import { useMemo, useRef } from "react";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import * as THREE from "three";
import { sceneState } from "../sceneState";
import { createIconTextures } from "./icons";

const POSES = [
  { t: 0, cam: [0.15, 0.2, 7.8], rot: 0.2, tilt: 0.04, y: 0.35, x: 0, scale: 1 },
  { t: 0.4, cam: [0.05, 0.55, 8.6], rot: 0.85, tilt: 0.1, y: 1.05, x: 0.15, scale: 0.7 },
  { t: 1, cam: [0.1, 0.35, 8.3], rot: 1.45, tilt: 0.02, y: 0.7, x: 0.08, scale: 0.62 },
];

function lerpPose(t) {
  const scroll = THREE.MathUtils.clamp(t, 0, 1);
  let from = POSES[0];
  let to = POSES[POSES.length - 1];
  for (let i = 0; i < POSES.length - 1; i += 1) {
    if (scroll >= POSES[i].t && scroll <= POSES[i + 1].t) {
      from = POSES[i];
      to = POSES[i + 1];
      break;
    }
  }
  const span = to.t - from.t || 1;
  const mix = THREE.MathUtils.smoothstep((scroll - from.t) / span, 0, 1);
  return {
    cam: from.cam.map((value, index) => THREE.MathUtils.lerp(value, to.cam[index], mix)),
    rot: THREE.MathUtils.lerp(from.rot, to.rot, mix),
    tilt: THREE.MathUtils.lerp(from.tilt, to.tilt, mix),
    y: THREE.MathUtils.lerp(from.y, to.y, mix),
    x: THREE.MathUtils.lerp(from.x, to.x, mix),
    scale: THREE.MathUtils.lerp(from.scale, to.scale, mix),
  };
}

function Dust({ count = 420 }) {
  const geometry = useMemo(() => {
    const positions = new Float32Array(count * 3);
    for (let i = 0; i < count; i += 1) {
      positions[i * 3] = (Math.random() - 0.5) * 14;
      positions[i * 3 + 1] = (Math.random() - 0.5) * 8;
      positions[i * 3 + 2] = (Math.random() - 0.5) * 7;
    }
    const geo = new THREE.BufferGeometry();
    geo.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    return geo;
  }, [count]);
  const ref = useRef(null);

  useFrame((_, delta) => {
    if (ref.current) ref.current.rotation.y += delta * 0.015;
  });

  return (
    <points ref={ref} geometry={geometry}>
      <pointsMaterial
        color="#c4a15a"
        size={0.02}
        transparent
        opacity={0.45}
        sizeAttenuation
        depthWrite={false}
      />
    </points>
  );
}

function IconOrbit({ icons, radius, speed, tilt, reduce }) {
  const spin = useRef(null);

  useFrame((_, delta) => {
    if (spin.current && !reduce) spin.current.rotation.y += delta * speed;
  });

  return (
    <group rotation={[tilt, 0, 0]}>
      <mesh rotation={[Math.PI / 2, 0, 0]}>
        <torusGeometry args={[radius, 0.006, 10, 140]} />
        <meshBasicMaterial color="#b8893d" transparent opacity={0.45} />
      </mesh>
      <group ref={spin}>
        {icons.map((icon, index) => {
          const angle = (index / icons.length) * Math.PI * 2;
          return (
            <sprite
              key={icon.name}
              position={[Math.cos(angle) * radius, 0, Math.sin(angle) * radius]}
              scale={[0.52, 0.52, 1]}
            >
              <spriteMaterial map={icon.map} transparent depthWrite={false} />
            </sprite>
          );
        })}
      </group>
    </group>
  );
}

function Studio() {
  const group = useRef(null);
  const { camera, size } = useThree();
  const icons = useMemo(() => createIconTextures(), []);
  const reduce = useMemo(
    () => window.matchMedia("(prefers-reduced-motion: reduce)").matches,
    []
  );

  useFrame((state, delta) => {
    const node = group.current;
    if (!node) return;
    const mobile = size.width < 860;
    const pose = lerpPose(reduce ? 0.15 : sceneState.scroll);
    const bob = reduce ? 0 : Math.sin(state.clock.elapsedTime * 0.55) * 0.05;
    const desiredX = (mobile ? 1.4 : 3.15) + pose.x + sceneState.pointer.x * 0.06;
    const desiredY = (mobile ? -0.4 : -1.15) + pose.y + bob - sceneState.pointer.y * 0.05;
    const desiredScale = (mobile ? 0.22 : 0.4) * pose.scale;

    node.position.x = THREE.MathUtils.damp(node.position.x, desiredX, 1.15, delta);
    node.position.y = THREE.MathUtils.damp(node.position.y, desiredY, 1.15, delta);
    node.rotation.y = THREE.MathUtils.damp(
      node.rotation.y,
      pose.rot + sceneState.pointer.x * 0.16,
      1.05,
      delta
    );
    node.rotation.x = THREE.MathUtils.damp(
      node.rotation.x,
      pose.tilt + sceneState.pointer.y * 0.06,
      1.05,
      delta
    );
    const nextScale = THREE.MathUtils.damp(node.scale.x, desiredScale, 1.15, delta);
    node.scale.setScalar(nextScale);

    camera.position.x = THREE.MathUtils.damp(
      camera.position.x,
      pose.cam[0] + sceneState.pointer.x * 0.12,
      1.05,
      delta
    );
    camera.position.y = THREE.MathUtils.damp(
      camera.position.y,
      pose.cam[1] - sceneState.pointer.y * 0.07,
      1.05,
      delta
    );
    camera.position.z = THREE.MathUtils.damp(camera.position.z, pose.cam[2], 1.05, delta);
    camera.lookAt(mobile ? 0 : 0.35, 0, 0);
  });

  return (
    <group ref={group} position={[1.42, 0.02, 0]}>
      <mesh>
        <sphereGeometry args={[0.28, 48, 48]} />
        <meshStandardMaterial color="#e8c98a" metalness={0.82} roughness={0.22} />
      </mesh>
      <mesh>
        <sphereGeometry args={[0.4, 32, 24]} />
        <meshBasicMaterial color="#c4a15a" wireframe transparent opacity={0.22} />
      </mesh>
      <IconOrbit
        icons={icons.slice(0, 4)}
        radius={1.05}
        speed={0.11}
        tilt={0.72}
        reduce={reduce}
      />
      <IconOrbit
        icons={icons.slice(4)}
        radius={1.48}
        speed={-0.065}
        tilt={1.12}
        reduce={reduce}
      />
    </group>
  );
}

function Scene() {
  return (
    <>
      <color attach="background" args={["#f7f1e8"]} />
      <fog attach="fog" args={["#f7f1e8", 9, 18]} />
      <ambientLight intensity={0.85} />
      <hemisphereLight args={["#fff6ee", "#e7c4a8", 0.55]} />
      <directionalLight position={[4, 6, 5]} intensity={1.35} color="#fff8f1" />
      <pointLight position={[1.8, 0.6, 2.4]} intensity={8} distance={10} color="#f0d7a2" />
      <Dust />
      <Studio />
    </>
  );
}

export default function World() {
  return (
    <Canvas
      className="world"
      camera={{ position: [0.05, 0.12, 7.4], fov: 38 }}
      dpr={[1, 1.5]}
      gl={{ antialias: true, alpha: false, powerPreference: "high-performance" }}
    >
      <Scene />
    </Canvas>
  );
}
