import { useEffect, useState } from "react";
import Lenis from "lenis";
import World from "./scene/World";
import { sceneState } from "./sceneState";
import {
  experience,
  profile,
  projects,
  portraitFiles,
  services,
  toolRows,
} from "./data";

const nav = [
  { href: "#about", label: "About" },
  { href: "#services", label: "What I do" },
  { href: "#work", label: "Work" },
  { href: "#experience", label: "Experience" },
];

function cutStudioBackground(img, keep = 0.7) {
  const w = img.naturalWidth;
  const h = img.naturalHeight;
  const canvas = document.createElement("canvas");
  canvas.width = w;
  canvas.height = h;
  const ctx = canvas.getContext("2d", { willReadFrequently: true });
  ctx.drawImage(img, 0, 0);
  const image = ctx.getImageData(0, 0, w, h);
  const data = image.data;
  const bg = new Uint8Array(w * h);
  const queue = new Int32Array(w * h);
  let head = 0;
  let tail = 0;

  const dark = (i) => {
    const o = i * 4;
    return Math.max(data[o], data[o + 1], data[o + 2]) <= 8;
  };

  const push = (x, y) => {
    const i = y * w + x;
    if (bg[i] || !dark(i)) return;
    bg[i] = 1;
    queue[tail] = i;
    tail += 1;
  };

  for (let x = 0; x < w; x += 1) {
    push(x, 0);
    push(x, h - 1);
  }
  for (let y = 0; y < h; y += 1) {
    push(0, y);
    push(w - 1, y);
  }

  while (head < tail) {
    const i = queue[head];
    head += 1;
    const x = i % w;
    const y = (i / w) | 0;
    if (x > 0) push(x - 1, y);
    if (x + 1 < w) push(x + 1, y);
    if (y > 0) push(x, y - 1);
    if (y + 1 < h) push(x, y + 1);
  }

  for (let i = 0; i < bg.length; i += 1) {
    const o = i * 4;
    if (bg[i]) data[o + 3] = 0;
  }

  for (let y = 1; y < h - 1; y += 1) {
    for (let x = 1; x < w - 1; x += 1) {
      const i = y * w + x;
      const o = i * 4;
      if (data[o + 3] === 0) continue;
      const lum = Math.max(data[o], data[o + 1], data[o + 2]);
      if (lum > 28) continue;
      const open =
        (data[(i - 1) * 4 + 3] === 0 ? 1 : 0) +
        (data[(i + 1) * 4 + 3] === 0 ? 1 : 0) +
        (data[(i - w) * 4 + 3] === 0 ? 1 : 0) +
        (data[(i + w) * 4 + 3] === 0 ? 1 : 0);
      if (open >= 3) data[o + 3] = 0;
      else if (open > 0 && lum < 18) data[o + 3] = Math.round((lum / 18) * 255);
    }
  }

  let minX = w;
  let minY = h;
  let maxX = 0;
  let maxY = 0;

  for (let i = 0; i < bg.length; i += 1) {
    if (data[i * 4 + 3] <= 18) continue;
    const x = i % w;
    const y = (i / w) | 0;
    if (x < minX) minX = x;
    if (y < minY) minY = y;
    if (x > maxX) maxX = x;
    if (y > maxY) maxY = y;
  }

  ctx.putImageData(image, 0, 0);
  if (maxX <= minX || maxY <= minY) return canvas.toDataURL("image/png");

  const pad = 12;
  const sx = Math.max(0, minX - pad);
  const sy = Math.max(0, minY - pad);
  const sw = Math.min(w - sx, maxX - minX + pad * 2);
  const sh = Math.min(h - sy, Math.round((maxY - minY) * keep) + pad);
  const out = document.createElement("canvas");
  out.width = sw;
  out.height = sh;
  out.getContext("2d").drawImage(canvas, sx, sy, sw, sh, 0, 0, sw, sh);
  return out.toDataURL("image/png");
}

function useCutout(file, keep) {
  const [src, setSrc] = useState(null);

  useEffect(() => {
    let cancelled = false;
    const img = new Image();
    img.onload = () => {
      if (!cancelled) setSrc(cutStudioBackground(img, keep));
    };
    img.src = file;
    return () => {
      cancelled = true;
    };
  }, [file, keep]);

  return src;
}

function usePortrait() {
  const [src, setSrc] = useState(null);

  useEffect(() => {
    let cancelled = false;

    const load = (file) =>
      new Promise((resolve) => {
        const img = new Image();
        img.onload = () => resolve(img);
        img.onerror = () => resolve(null);
        img.src = file;
      });

    (async () => {
      for (const file of portraitFiles) {
        const img = await load(file);
        if (!img || cancelled) continue;
        setSrc(cutStudioBackground(img));
        return;
      }
    })();

    return () => {
      cancelled = true;
    };
  }, []);

  return src;
}

function useActiveSection() {
  const [active, setActive] = useState("");

  useEffect(() => {
    const sections = ["about", "services", "work", "experience", "contact"]
      .map((id) => document.getElementById(id))
      .filter(Boolean);

    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
        if (visible) setActive(visible.target.id);
      },
      { rootMargin: "-40% 0px -45% 0px", threshold: [0.1, 0.25, 0.5] }
    );

    sections.forEach((section) => observer.observe(section));
    return () => observer.disconnect();
  }, []);

  return active;
}

export default function App() {
  const portrait = usePortrait();
  const aboutPhoto = useCutout("/about.png", 1);
  const active = useActiveSection();
  const [booted, setBooted] = useState(false);
  const [copied, setCopied] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const timer = window.setTimeout(() => setBooted(true), 700);
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    const revealNodes = document.querySelectorAll("[data-reveal]");
    const serviceBits = document.querySelectorAll(".services h2, .services li");
    const experienceBits = document.querySelectorAll(".experience-head, .steps > li");
    const hero = document.querySelector(".hero");
    const setReveal = (node) => {
      if (reduce) {
        node.style.setProperty("--reveal", "1");
        return;
      }
      const top = node.getBoundingClientRect().top;
      const start = window.innerHeight * Number(node.dataset.revealStart || 0.92);
      const end = window.innerHeight * Number(node.dataset.revealEnd || 0.42);
      const progress = (start - top) / (start - end);
      node.style.setProperty("--reveal", Math.min(1, Math.max(0, progress)).toFixed(3));
    };

    const setServiceMotion = (node) => {
      if (reduce) {
        node.style.setProperty("--show", "1");
        return;
      }
      const top = node.getBoundingClientRect().top;
      const start = window.innerHeight * 0.96;
      const end = window.innerHeight * 0.58;
      const progress = (start - top) / (start - end);
      node.style.setProperty("--show", Math.min(1, Math.max(0, progress)).toFixed(3));
    };

    const syncScroll = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      sceneState.scroll = max > 0 ? window.scrollY / max : 0;
      const bar = document.querySelector(".progress");
      if (bar) bar.style.transform = `scaleX(${sceneState.scroll})`;
      revealNodes.forEach(setReveal);
      serviceBits.forEach(setServiceMotion);
      experienceBits.forEach((node) => {
        if (reduce) {
          node.style.setProperty("--show", "1");
          return;
        }
        const top = node.getBoundingClientRect().top;
        const start = window.innerHeight * 0.98;
        const end = window.innerHeight * 0.72;
        const progress = (start - top) / (start - end);
        node.style.setProperty("--show", Math.min(1, Math.max(0, progress)).toFixed(3));
      });
      if (hero) {
        const drift = reduce ? 0 : Math.min(window.scrollY, window.innerHeight * 0.85);
        hero.style.setProperty("--drift", `${drift.toFixed(1)}px`);
      }
    };

    const onMove = (event) => {
      if (reduce) return;
      sceneState.pointer.x = (event.clientX / window.innerWidth) * 2 - 1;
      sceneState.pointer.y = (event.clientY / window.innerHeight) * 2 - 1;
    };

    const lenis = reduce
      ? null
      : new Lenis({
          autoRaf: true,
          lerp: 0.055,
          smoothWheel: true,
          wheelMultiplier: 0.85,
        });
    lenis?.on("scroll", syncScroll);

    const onAnchor = (event) => {
      const link = event.target.closest?.("a[href^='#']");
      if (!link || !lenis) return;
      const target = document.querySelector(link.getAttribute("href"));
      if (!target) return;
      event.preventDefault();
      const offset = target.id === "top" ? 0 : -84;
      lenis.scrollTo(target, { offset, duration: 1.35 });
    };

    const stage = document.querySelector(".reel-stage");
    const track = stage?.querySelector(".reel-track");
    let reelFrame = 0;
    let reelOffset = 0;
    let reelLast = performance.now();
    const tickReel = (now) => {
      if (track && stage) {
        const cards = [...track.children];
        const loopAt = cards[cards.length / 2]?.offsetLeft || track.scrollWidth / 2;
        const delta = Math.min(32, now - reelLast);
        reelLast = now;
        if (loopAt > 0) {
          reelOffset = (reelOffset + (loopAt / 28000) * delta) % loopAt;
        }
        track.style.transform = `translate3d(${-reelOffset}px,0,0)`;
        const mid = stage.getBoundingClientRect().left + stage.clientWidth / 2;
        const reach = stage.clientWidth * 0.42;
        const trackLeft = track.getBoundingClientRect().left;
        const width = cards[0]?.offsetWidth || 1;
        const centers = cards.map((card) => trackLeft + card.offsetLeft + width / 2);
        const ranked = centers
          .map((center, index) => ({ index, dist: Math.abs(center - mid) }))
          .sort((a, b) => a.dist - b.dist);
        const primary = ranked[0].index;
        const scales = centers.map((center) => {
          const distance = Math.min(1, Math.abs(center - mid) / reach);
          return 1.12 - distance * 0.34;
        });
        const shift = new Array(cards.length).fill(0);
        for (let index = primary; index < cards.length - 1; index += 1) {
          shift[index + 1] = shift[index] + width * ((scales[index] + scales[index + 1]) / 2 - 1);
        }
        for (let index = primary; index > 0; index -= 1) {
          shift[index - 1] = shift[index] - width * ((scales[index - 1] + scales[index]) / 2 - 1);
        }
        cards.forEach((card, index) => {
          const distance = Math.min(1, Math.abs(centers[index] - mid) / reach);
          card.style.setProperty("--focus", scales[index].toFixed(3));
          card.style.setProperty("--shift", `${shift[index].toFixed(1)}px`);
          card.style.setProperty("--blur", `${(distance * distance * 2.4).toFixed(2)}px`);
        });
      }
      reelFrame = window.requestAnimationFrame(tickReel);
    };
    if (!reduce && track) reelFrame = window.requestAnimationFrame(tickReel);

    syncScroll();
    window.addEventListener("scroll", syncScroll, { passive: true });
    window.addEventListener("pointermove", onMove, { passive: true });
    document.addEventListener("click", onAnchor);
    return () => {
      window.clearTimeout(timer);
      window.cancelAnimationFrame(reelFrame);
      lenis?.destroy();
      window.removeEventListener("scroll", syncScroll);
      window.removeEventListener("pointermove", onMove);
      document.removeEventListener("click", onAnchor);
    };
  }, []);

  async function copyEmail() {
    try {
      await navigator.clipboard.writeText(profile.email);
      setCopied(true);
      window.setTimeout(() => setCopied(false), 1600);
    } catch {
      window.location.href = `mailto:${profile.email}`;
    }
  }

  return (
    <>
      <World />
      <div className="scrim" />
      <div className="progress" />
      <div className={`loader ${booted ? "gone" : ""}`} aria-hidden={booted}>
        <span>ASWIN K</span>
      </div>

      <header className={`nav${menuOpen ? " is-open" : ""}`}>
        <a className="brand" href="#top" onClick={() => setMenuOpen(false)}>
          <img src="/ak-mark.png?v=2" alt="" />
          ASWIN K.
        </a>
        <button
          type="button"
          className="nav-toggle"
          aria-expanded={menuOpen}
          aria-label={menuOpen ? "Close menu" : "Open menu"}
          onClick={() => setMenuOpen((open) => !open)}
        >
          <span />
          <span />
        </button>
        <nav>
          {nav.map((item) => (
            <a
              key={item.href}
              href={item.href}
              className={active === item.href.slice(1) ? "is-active" : ""}
              onClick={() => setMenuOpen(false)}
            >
              {item.label}
            </a>
          ))}
        </nav>
        <a className="talk" href="#contact" onClick={() => setMenuOpen(false)}>
          Let’s talk <i>→</i>
        </a>
      </header>

      <main id="top">
        <section className="hero">
          <div className="hero-copy">
            <p className="eyebrow">
              Hi, I’m Aswin K
              <span className="spark">✦</span>
            </p>
            <h1>
              <span className="soft">Python</span>
              <span className="strong">Developer</span>
              <span className="spark">+</span>
            </h1>
            <p className="hero-kicker">& Data Scientist</p>
            <p className="lede">
              I build React Websites, Backend Systems, Data Pipelines & Computer-Vision tools.
            </p>
            <div className="hero-actions">
              <a className="btn" href="#work">
                View work <i>→</i>
              </a>
            </div>
            <ul className="hero-chips">
              <li>Python</li>
              <li>Django</li>
              <li>React</li>
              <li>Data Science</li>
              <li>Machine Learning</li>
            </ul>
          </div>

          <div className="hero-visual">
            <div className="blob" />
            <span className="orbit" aria-hidden="true" />
            <span className="mark" aria-hidden="true">✦</span>
            <svg className="sprig" viewBox="0 0 90 150" aria-hidden="true">
              <path d="M46 142c2-34-2-62 6-104" stroke="#8ea184" strokeWidth="1.4" fill="none" />
              <path d="M52 46c22-10 34-22 30-34-16 6-26 18-30 34Z" fill="#c9d4b6" />
              <path d="M50 70C30 60 16 48 20 34c16 8 26 22 30 36Z" fill="#b7c6a6" />
              <path d="M54 98c22-6 36-20 32-34-16 8-28 22-32 34Z" fill="#d7e0c8" />
            </svg>
            {portrait ? (
              <img src={portrait} alt="Portrait of Aswin K" />
            ) : (
              <strong className="fallback">ASWIN K</strong>
            )}
            <div className="smoke" aria-hidden="true" />
          </div>
        </section>

        <section className="about" id="about" data-reveal data-reveal-start="0.92" data-reveal-end="0.4">
          <div className="about-head">
            <p className="label">About me</p>
            <h2>
              I build software
              <em> that ships.</em>
            </h2>
          </div>
          <div className="about-photo">
            <div className="about-blob" />
            {aboutPhoto ? (
              <img src={aboutPhoto} alt="Aswin K seated in a studio portrait" />
            ) : null}
            <div className="about-smoke" aria-hidden="true" />
          </div>
          <div className="about-copy">
            <p>{profile.summary}</p>
            <p>
            While leading development and data initiatives at Natdemy,
             I regularly partner with select clients as an independent contractor. 
             I help teams validate ideas quickly, automate manual operations, 
             and ship production-grade software without the overhead of a full agency. 
            Have a project in mind? Let’s build it right.
            </p>
          </div>
        </section>

        <div className="sheet">
          <section className="block services" id="services" data-reveal>
            <h2>
              What I do
              <em> for clients.</em>
            </h2>
            <ol>
              {services.map((item, index) => (
                <li key={item.title} style={{ "--step": index * 0.08 }}>
                  <span>{String(index + 1).padStart(2, "0")}</span>
                  <h3>{item.title}</h3>
                  <p>{item.text}</p>
                </li>
              ))}
            </ol>
          </section>

          <section className="block work" id="work" data-reveal>
            <div className="work-head">
              <h2>
                Projects
                <em> from the work.</em>
              </h2>
            </div>
            <div className="reel-stage">
              <div className="reel-track">
                {[0, 1].map((copy) =>
                  projects.map((project, index) => {
                    const body = (
                      <>
                        <small>{String(index + 1).padStart(2, "0")}</small>
                        <h3>{project.title}</h3>
                        <p>{project.summary}</p>
                        <span>{project.stack.join(" · ")}</span>
                      </>
                    );
                    const key = `${project.title}-${copy}`;
                    return project.href ? (
                      <a
                        className="reel-card"
                        key={key}
                        href={project.href}
                        target="_blank"
                        rel="noreferrer"
                        tabIndex={copy ? -1 : undefined}
                        aria-hidden={copy ? "true" : undefined}
                      >
                        {body}
                      </a>
                    ) : (
                      <article className="reel-card" key={key} aria-hidden={copy ? "true" : undefined}>
                        {body}
                      </article>
                    );
                  })
                )}
              </div>
            </div>
          </section>

          <section className="block tools" id="tools" data-reveal>
            <h2>
              Tools
              <em> familiar.</em>
            </h2>
            <div className="tool-rows">
              {toolRows.map((row, rowIndex) => (
                <div className={rowIndex === 0 ? "tool-row ltr" : "tool-row rtl"} key={rowIndex}>
                  <div className="tool-track">
                    {[0, 1].map((copy) =>
                      [0, 1, 2, 3].map((repeat) =>
                        row.map((tool) => (
                          <div
                            className="tool-box"
                            key={`${tool.name}-${copy}-${repeat}`}
                            aria-hidden={copy || repeat ? "true" : undefined}
                          >
                            <img src={tool.src} alt={copy || repeat ? "" : tool.name} />
                          </div>
                        ))
                      )
                    )}
                  </div>
                </div>
              ))}
            </div>
          </section>

          <section className="block" id="experience" data-reveal>
            <div className="panel">
              <div className="experience-head">
                <p className="label">Experience</p>
                <h2>
                  Where I’ve worked
                  <em> so far.</em>
                </h2>
              </div>
              <ol className="steps">
                {experience.map((job, index) => (
                  <li key={job.org} style={{ "--step": index * 0.12 }}>
                    <span>{String(index + 1).padStart(2, "0")}</span>
                    {job.logo ? (
                      <span className={job.logoDark ? "org-mark dark" : "org-mark"}>
                        <img src={job.logo} alt="" />
                      </span>
                    ) : (
                      <span className="org-mark" aria-hidden="true" />
                    )}
                    <div>
                      <h3>{job.role}</h3>
                      <p className="where">
                        {job.org}
                        {job.dates ? ` · ${job.dates}` : ""}
                      </p>
                    </div>
                    <p className="line">{job.line}</p>
                  </li>
                ))}
              </ol>
            </div>
          </section>

          <section className="banner" id="contact">
            <div>
              <h2>
                Let’s build
                <em> something precise.</em>
              </h2>
            </div>
            <div className="banner-copy">
              <p>Open to Python and data science work.</p>
              <a className="talk solid" href={`mailto:${profile.email}`}>
                Let’s work together <i>→</i>
              </a>
              <div className="contact-links">
                <button type="button" onClick={copyEmail}>
                  {copied ? "Copied" : profile.email}
                </button>
                <a href={profile.phoneHref} target="_blank" rel="noreferrer">
                  {profile.phone}
                </a>
                <a href={profile.linkedin} target="_blank" rel="noreferrer">
                  LinkedIn
                </a>
                <a href={profile.github} target="_blank" rel="noreferrer">
                  GitHub
                </a>
              </div>
            </div>
          </section>

          <footer>
            <span>Aswin K</span>
            <span>Python Developer & Data Scientist</span>
          </footer>
        </div>
      </main>
    </>
  );
}
