document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('wheel');
    const spinButton = document.getElementById('spin');
    const results = document.getElementById('results');
    const ctx = canvas.getContext('2d');
    const dia = ctx.canvas.width;
    const rad = dia / 2;
    const PI = Math.PI;
    const TAU = 2 * PI;
    let sectors = [];
    let angVel = 0; // Angular velocity
    let ang = 0; // Angle in radians

    const rand = (m, M) => Math.random() * (M - m) + m;
    const tot = () => sectors.length;
    const arc = () => TAU / tot();
    const friction = 0.991; // 0.995=soft, 0.99=mid, 0.98=hard

    const getIndex = () => Math.floor(tot() - (ang / TAU) * tot()) % tot();

    function drawSector(sector, i) {
        const ang = arc() * i;
        ctx.save();
        ctx.beginPath();
        ctx.fillStyle = sector.color;
        ctx.moveTo(rad, rad);
        ctx.arc(rad, rad, rad, ang, ang + arc());
        ctx.lineTo(rad, rad);
        ctx.fill();
        ctx.translate(rad, rad);
        ctx.rotate(ang + arc() / 2);
        ctx.textAlign = 'right';
        ctx.fillStyle = '#fff';
        ctx.font = 'bold 30px sans-serif';
        ctx.fillText(sector.label, rad - 10, 10);
        ctx.restore();
    }

    function rotate() {
        if (sectors.length === 0) return; // Sprawdzenie, czy są sektory
        const sector = sectors[getIndex()];
        ctx.canvas.style.transform = `rotate(${ang - PI / 2}rad)`;
        spinButton.textContent = !angVel ? 'SPIN' : sector.label;
        spinButton.style.background = sector.color;

        if(angVel===0 && sector){
            const resultDiv = document.createElement('div');
            resultDiv.className = 'container'
            resultDiv.style.backgroundColor = sector.color;
            resultDiv.textContent = sector.label;
            results.appendChild(resultDiv);
        }
    }

    function frame() {
        if (!angVel) return;
        angVel *= friction;
        if (angVel < 0.002) angVel = 0;
        ang += angVel;
        ang %= TAU;
        rotate();
    }

    function engine() {
        frame();
        requestAnimationFrame(engine);
    }

    function init() {
        if (sectors.length > 0) {
            sectors.forEach(drawSector);
            rotate();
        }
        engine();
        spinButton.addEventListener('click', () => {
            if (!angVel && sectors.length > 0) angVel = rand(0.25, 0.45);
        });
    }

    // Event listener for adding new options
    document.getElementById('add-option').addEventListener('click', () => {
        const label = document.getElementById('option-label').value;
        const color = "#"+Math.floor(Math.random()*16777215).toString(16);
        if (label && color) {
            sectors.push({ label, color });
            ctx.clearRect(0, 0, dia, dia);
            sectors.forEach(drawSector);
            document.getElementById('option-label').value = '';
        }
    });

    init();
});
