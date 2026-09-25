export const profile = {
  name: "Aswin K",
  role: "Python Developer & Data Scientist",
  location: "Kannur, Kerala",
  email: "aswinkandambeth113@gmail.com",
  phone: "+91 7994092238",
  phoneHref: "https://wa.me/917994092238",
  github: "https://github.com/aswink113",
  linkedin: "https://www.linkedin.com/in/aswin-k113",
  summary:
    "Modern software isn't just about code—it’s about speed, reliability, and business outcomes. With deep experience spanning Python, Django, React, and Machine Learning pipelines, I turn complicated workflows into intuitive, resilient digital products..",
};

export const portraitFiles = [
  "/portrait.jpg",
  "/portrait.jpeg",
  "/portrait.png",
  "/portrait.webp",
];

export const experience = [
  {
    role: "Data Scientist & Python Developer",
    org: "NATDEMY",
    logo: "/companies/natdemy-word.png",
    place: "Parappanangadi",
    dates: "Nov 2025 — Present",
    line: "I build the ERP and learning products in Python, Django, and React.",
  },
  {
    role: "Data Science & Machine Learning Intern",
    org: "CAMERINFOLKS",
    logo: "/companies/camerin-clear.png",
    place: "Kakkanad",
    dates: "May 2025 — Nov 2025",
    line: "I built data and machine-learning pipelines for real business problems.",
  },
  {
    role: "Telecom Engineer",
    org: "IMMCO Inc.",
    logo: "/companies/immco-clear.png",
    dates: "Jan 2022 — Aug 2023",
    line: "I planned FTTP and FTTx networks, and N2P designs in GIS and CAD.",
  },
];

export const services = [
  {
    title: "Web applications",
    text: "React interfaces and company sites, including dashboards and a headless CMS so teams can update content themselves.",
  },
  {
    title: "Backend systems",
    text: "Django and REST services, with PostgreSQL schemas built for finance, HR, inventory, and learning products.",
  },
  {
    title: "Data & machine learning",
    text: "Pipelines from preprocessing through model building and evaluation, applied to real business problems.",
  },
  {
    title: "Computer vision",
    text: "Detection models with YOLO, OpenCV, and CNNs, including real-time checks on drone and camera footage.",
  },
  {
    title: "AI video generating",
    text: "Short videos produced with AI tools, from a brief through generated scenes, voice, and a cut ready to publish.",
  },
  {
    title: "Video editing",
    text: "Edits in CapCut for reels and explainers: pacing, captions, and a clean finish that matches the brand.",
  },
];

export const toolRows = [
  [
    { name: "Python", src: "/logos/python.jpg" },
    { name: "Django", src: "/logos/django.jpg" },
    { name: "React", src: "/logos/react.jpg" },
    { name: "HTML", src: "/logos/html.jpg" },
    { name: "Git", src: "/logos/Git.jpg" },
    { name: "GitHub", src: "/logos/github.jpg" },
    { name: "Postman", src: "/logos/postman.jpg" },
  ],
  [
    { name: "ChatGPT", src: "/logos/chatgpt.jpg" },
    { name: "Gemini", src: "/logos/gemini.jpg" },
    { name: "Cursor", src: "/logos/cursor.jpg" },
    { name: "Antigravity", src: "/logos/antigravity.jpg" },
    { name: "Canva", src: "/logos/canva.jpg" },
    { name: "CapCut", src: "/logos/CapCut.jpg" },
    { name: "LinkedIn", src: "/logos/linedin.jpg" },
  ],
];

export const projects = [
  {
    title: "Enterprise Resource Planning",
    summary:
      "Full-stack ERP across finance, HR, and inventory. PostgreSQL indexing and a normalized schema cut data retrieval time by 40%, with real-time sync between modules.",
    stack: ["Django", "React", "PostgreSQL", "REST"],
    href: "https://github.com/aswink113/ERP-SYSTEM",
    color: "#a67c3d",
  },
  {
    title: "Asset Management System",
    summary:
      "Digital tracking for corporate asset lifecycles, with automated depreciation and maintenance alerts over REST. A React dashboard shows live allocation and reduces equipment loss.",
    stack: ["React", "REST APIs", "Python"],
    color: "#8d6239",
  },
  {
    title: "River Plastic Waste Detection",
    summary:
      "Real-time detection on drone footage. A YOLO / CNN model, tuned for shifting light and water, finds floating plastic and exports categorized counts to CSV.",
    stack: ["Python", "YOLO", "OpenCV", "CNN"],
    href: "https://github.com/aswink113/PLASTIC-WASTE-DETECTION-FROM-RIVER",
    color: "#b08948",
  },
  {
    title: "Smart Attendance System",
    summary:
      "Fraud-resistant attendance for classrooms and staff. Python watches engagement and punctuality in real time, and automated triggers replace manual entry.",
    stack: ["Python", "Automation"],
    href: "https://github.com/aswink113/SMART-ATTENDANCE-SYSTEM",
    color: "#c4a46a",
  },
  {
    title: "LMS Application",
    summary:
      "EdTech for interactive English learning and NIOS / SSLC curriculum support. The backend and learning interface deliver structured lessons, activity monitoring, and progress tracking.",
    stack: ["Python", "Django", "DRF"],
    color: "#9a7044",
  },
  {
    title: "Corporate Website",
    summary:
      "Responsive, SEO-minded company site in React and Tailwind, with a headless CMS so non-technical staff can update work and services without touching code.",
    stack: ["React", "Tailwind CSS", "Headless CMS"],
    color: "#7a5a32",
  },
];
