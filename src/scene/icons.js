import * as THREE from "three";

function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.roundRect(x, y, w, h, r);
}

function base(ctx) {
  ctx.clearRect(0, 0, 256, 256);
  ctx.save();
  ctx.shadowColor = "rgba(120, 72, 32, 0.22)";
  ctx.shadowBlur = 18;
  ctx.shadowOffsetY = 8;
  ctx.beginPath();
  ctx.arc(128, 128, 112, 0, Math.PI * 2);
  ctx.fillStyle = "#ffffff";
  ctx.fill();
  ctx.restore();
  ctx.beginPath();
  ctx.arc(128, 128, 112, 0, Math.PI * 2);
  ctx.lineWidth = 10;
  ctx.strokeStyle = "#a67c3d";
  ctx.stroke();
}

function caption(ctx, text) {
  ctx.fillStyle = "#5c4030";
  ctx.font = "600 18px Outfit, sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(text, 128, 200);
}

function drawPython(ctx) {
  base(ctx);
  ctx.fillStyle = "#ffd343";
  roundRect(ctx, 90, 58, 42, 78, 20);
  ctx.fill();
  ctx.fillStyle = "#3776ab";
  roundRect(ctx, 122, 82, 42, 78, 20);
  ctx.fill();
  ctx.fillStyle = "#fffaf6";
  ctx.beginPath();
  ctx.arc(110, 80, 5, 0, Math.PI * 2);
  ctx.arc(144, 140, 5, 0, Math.PI * 2);
  ctx.fill();
  caption(ctx, "Python");
}

function drawReact(ctx) {
  base(ctx);
  ctx.save();
  ctx.translate(128, 108);
  ctx.strokeStyle = "#149eca";
  ctx.lineWidth = 7;
  [0, Math.PI / 3, -Math.PI / 3].forEach((angle) => {
    ctx.beginPath();
    ctx.ellipse(0, 0, 58, 22, angle, 0, Math.PI * 2);
    ctx.stroke();
  });
  ctx.fillStyle = "#149eca";
  ctx.beginPath();
  ctx.arc(0, 0, 8, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
  caption(ctx, "React");
}

function drawDjango(ctx) {
  base(ctx);
  ctx.fillStyle = "#0c4b33";
  roundRect(ctx, 78, 58, 100, 88, 18);
  ctx.fill();
  ctx.fillStyle = "#f4efe6";
  ctx.font = "700 42px Georgia, serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText("dj", 128, 102);
  caption(ctx, "Django");
}

function drawPostgres(ctx) {
  base(ctx);
  ctx.strokeStyle = "#336791";
  ctx.fillStyle = "#336791";
  ctx.lineWidth = 7;
  ctx.beginPath();
  ctx.ellipse(128, 78, 36, 14, 0, 0, Math.PI * 2);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(92, 78);
  ctx.lineTo(92, 128);
  ctx.ellipse(128, 128, 36, 14, 0, Math.PI, 0, true);
  ctx.lineTo(164, 78);
  ctx.stroke();
  ctx.beginPath();
  ctx.ellipse(128, 104, 36, 14, 0, 0, Math.PI * 2);
  ctx.stroke();
  caption(ctx, "Postgres");
}

function drawTensor(ctx) {
  base(ctx);
  ctx.fillStyle = "#ff6f00";
  ctx.beginPath();
  ctx.moveTo(128, 58);
  ctx.lineTo(176, 86);
  ctx.lineTo(176, 140);
  ctx.lineTo(128, 168);
  ctx.lineTo(80, 140);
  ctx.lineTo(80, 86);
  ctx.closePath();
  ctx.fill();
  ctx.fillStyle = "#fffaf6";
  ctx.font = "700 36px Outfit, sans-serif";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText("TF", 128, 114);
  caption(ctx, "TensorFlow");
}

function drawGit(ctx) {
  base(ctx);
  ctx.strokeStyle = "#f05033";
  ctx.fillStyle = "#f05033";
  ctx.lineWidth = 7;
  ctx.lineCap = "round";
  ctx.beginPath();
  ctx.moveTo(108, 70);
  ctx.lineTo(108, 150);
  ctx.moveTo(108, 104);
  ctx.lineTo(150, 104);
  ctx.lineTo(150, 78);
  ctx.stroke();
  [ [108, 70], [108, 150], [150, 78] ].forEach(([x, y]) => {
    ctx.beginPath();
    ctx.arc(x, y, 8, 0, Math.PI * 2);
    ctx.fill();
  });
  caption(ctx, "Git");
}

function drawTailwind(ctx) {
  base(ctx);
  ctx.strokeStyle = "#38bdf8";
  ctx.lineWidth = 8;
  ctx.lineCap = "round";
  ctx.lineJoin = "round";
  ctx.beginPath();
  ctx.moveTo(72, 118);
  ctx.bezierCurveTo(90, 86, 108, 86, 118, 104);
  ctx.bezierCurveTo(128, 122, 146, 128, 164, 108);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(92, 142);
  ctx.bezierCurveTo(110, 110, 128, 110, 138, 128);
  ctx.bezierCurveTo(148, 146, 166, 152, 184, 132);
  ctx.stroke();
  caption(ctx, "Tailwind");
}

function drawVision(ctx) {
  base(ctx);
  ctx.strokeStyle = "#2f6f4e";
  ctx.fillStyle = "#2f6f4e";
  ctx.lineWidth = 7;
  ctx.beginPath();
  ctx.ellipse(128, 112, 52, 28, 0, 0, Math.PI * 2);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(128, 112, 12, 0, Math.PI * 2);
  ctx.fill();
  caption(ctx, "OpenCV");
}

function texture(draw) {
  const canvas = document.createElement("canvas");
  canvas.width = 256;
  canvas.height = 256;
  const ctx = canvas.getContext("2d");
  draw(ctx);
  const map = new THREE.CanvasTexture(canvas);
  map.colorSpace = THREE.SRGBColorSpace;
  map.anisotropy = 8;
  map.needsUpdate = true;
  return map;
}

export function createIconTextures() {
  return [
    { name: "Python", map: texture(drawPython) },
    { name: "React", map: texture(drawReact) },
    { name: "Django", map: texture(drawDjango) },
    { name: "Postgres", map: texture(drawPostgres) },
    { name: "TensorFlow", map: texture(drawTensor) },
    { name: "Git", map: texture(drawGit) },
    { name: "Tailwind", map: texture(drawTailwind) },
    { name: "OpenCV", map: texture(drawVision) },
  ];
}
