(function () {
    const cfg = window.QUIZ_CONFIG;
    const $ = (id) => document.getElementById(id);

    const screens = {
        start: $("screen-start"),
        question: $("screen-question"),
        result: $("screen-result")
    };
    const bgLayers = [document.querySelector(".bg-a"), document.querySelector(".bg-b")];
    const optionsEl = document.querySelector(".options");
    const optionBtns = { A: optionsEl.querySelector(".option-a"), B: optionsEl.querySelector(".option-b") };

    const questions = cfg.totalQuestions
        ? cfg.questions.slice(0, cfg.totalQuestions)
        : cfg.questions;

    let index = 0;
    let score = { A: 0, B: 0 };
    let activeBg = 0;

    // --- Sfondi ---
    function toCssBackground(value) {
        const v = (value || cfg.defaultBackground || "").trim();
        if (/^(linear|radial|conic|repeating-)/i.test(v) || /^(#|rgb|hsl)/i.test(v) || /^[a-z]+$/i.test(v)) {
            return v;
        }
        return `url("${v}")`;
    }

    function setBackground(value) {
        const next = 1 - activeBg;
        bgLayers[next].style.background = toCssBackground(value);
        bgLayers[next].style.backgroundSize = "cover";
        bgLayers[next].style.backgroundPosition = "center";
        bgLayers[next].classList.add("active");
        bgLayers[activeBg].classList.remove("active");
        activeBg = next;
    }

    // --- Schermate ---
    function show(name) {
        Object.entries(screens).forEach(([key, el]) => {
            el.classList.remove("active", "leaving");
            if (key === name) {
                void el.offsetWidth; // riavvia l'animazione
                el.classList.add("active");
            }
        });
    }

    function renderQuestion() {
        const q = questions[index];
        $("question-text").textContent = q.question;
        optionBtns.A.querySelector(".label").textContent = q.optionA;
        optionBtns.B.querySelector(".label").textContent = q.optionB;
        optionsEl.classList.remove("locked");
        Object.values(optionBtns).forEach((b) => b.classList.remove("chosen"));

        $("progress-fill").style.width = `${(index / questions.length) * 100}%`;
        $("progress-text").textContent = `${index + 1}/${questions.length}`;
        setBackground(q.background);
        show("question");
    }

    function choose(option) {
        if (optionsEl.classList.contains("locked")) return;
        optionsEl.classList.add("locked");
        optionBtns[option].classList.add("chosen");
        score[option]++;
        $("progress-fill").style.width = `${((index + 1) / questions.length) * 100}%`;

        setTimeout(() => {
            screens.question.classList.add("leaving");
            setTimeout(() => {
                index++;
                index < questions.length ? renderQuestion() : showResult();
            }, 350);
        }, 450);
    }

    function showResult() {
        let winner;
        if (score.A === score.B) winner = cfg.tieBreaker === "B" ? "B" : "A";
        else winner = score.A > score.B ? "A" : "B";

        const gift = cfg.gifts[winner];
        $("gift-image").src = gift.image;
        $("gift-title").textContent = gift.title;
        $("gift-message").textContent = gift.message;

        const box = $("gift-box");
        box.classList.remove("open");
        screens.result.classList.remove("revealed");
        setBackground(cfg.defaultBackground);
        show("result");
        setTimeout(() => {
            box.classList.add("open");
            screens.result.classList.add("revealed");
            launchConfetti();
        }, 1600);
    }

    function start() {
        index = 0;
        score = { A: 0, B: 0 };
        renderQuestion();
    }

    // --- Elementi fluttuanti ---
    function createFloaters() {
        const symbols = ["💖", "✨", "🎈", "💜", "⭐", "🎀"];
        const host = document.querySelector(".floaters");
        for (let i = 0; i < 16; i++) {
            const el = document.createElement("span");
            el.className = "floater";
            el.textContent = symbols[i % symbols.length];
            el.style.left = `${Math.random() * 100}%`;
            el.style.fontSize = `${18 + Math.random() * 26}px`;
            el.style.animationDuration = `${9 + Math.random() * 10}s`;
            el.style.animationDelay = `${-Math.random() * 15}s`;
            host.appendChild(el);
        }
    }

    // --- Coriandoli ---
    function launchConfetti() {
        const canvas = $("confetti");
        const ctx = canvas.getContext("2d");
        canvas.width = innerWidth;
        canvas.height = innerHeight;
        const colors = ["#ff5c8a", "#7c5cff", "#ffd166", "#06d6a0", "#4cc9f0"];
        const pieces = Array.from({ length: 160 }, () => ({
            x: canvas.width / 2,
            y: canvas.height * 0.45,
            vx: (Math.random() - 0.5) * 16,
            vy: -Math.random() * 16 - 4,
            size: 6 + Math.random() * 8,
            rot: Math.random() * Math.PI,
            vr: (Math.random() - 0.5) * 0.4,
            color: colors[Math.floor(Math.random() * colors.length)]
        }));
        let frames = 0;
        (function tick() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            pieces.forEach((p) => {
                p.vy += 0.3;
                p.x += p.vx;
                p.y += p.vy;
                p.rot += p.vr;
                ctx.save();
                ctx.translate(p.x, p.y);
                ctx.rotate(p.rot);
                ctx.fillStyle = p.color;
                ctx.fillRect(-p.size / 2, -p.size / 4, p.size, p.size / 2);
                ctx.restore();
            });
            if (++frames < 200) requestAnimationFrame(tick);
            else ctx.clearRect(0, 0, canvas.width, canvas.height);
        })();
    }

    // --- Init ---
    document.title = cfg.title;
    $("quiz-title").textContent = cfg.title;
    $("quiz-subtitle").textContent = cfg.subtitle;
    $("start-btn").textContent = cfg.startButton;
    setBackground(cfg.defaultBackground);
    createFloaters();

    $("start-btn").addEventListener("click", start);
    optionBtns.A.addEventListener("click", () => choose("A"));
    optionBtns.B.addEventListener("click", () => choose("B"));
})();
