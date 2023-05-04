class Carta {
    constructor(random) {
        let valore = random % 13 + 1
        let seme = Math.floor(random / 13)
        switch (seme) {
            case 0:
                seme = "C";
                break;
            case 1:
                seme = "Q";
                break;
            case 2:
                seme = "F";
                break;
            case 3:
                seme = "P";
                break;
        }
        let html = /*html*/ `<img src="Cards/${valore}${seme}.PNG">`
        tappetino.innerHTML += html;
    }
}

class Mazzo {
    mazzo = []

    constructor() {
        this.Mescola()
    }

    Mescola() {
        this.mazzo = []
        for (let i = 0; i < 52; i++) {
            this.mazzo.push(0)
        }
    }

    Pesca() {
        let r;
        while (true) {
            r = Math.random() * 52;
            r = Math.floor(r);
            if (this.mazzo[r] < 1) {
                this.mazzo[r]++;
                break;
            } else {
                continue;
            }
        }
        new Carta(r);
    }
}