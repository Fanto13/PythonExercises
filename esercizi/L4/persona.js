class Persona {
    nome;
    cognome;
    eta = 0;

    static bigbang = 13000000000;

    constructor(nome, cognome) {
        this.nome = nome;
        this.cognome = cognome;
    }

    dormi() {
        console.log("sto dormendo!")
    }

    mangia() {
        console.log("sto mangiando!")
    }

    invecchia() {
        this.eta++
    }

    get CF() {
        return this.cognome + this.nome + this.eta
    }

    static matrimonio(persona1, persona2) {
        persona1.coniuge = persona2
        persona2.coniuge = persona1
    }
}