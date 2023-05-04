class Studente extends Persona {
    scuola;

    constructor(nome, cognome, scuola) {
        super(nome, cognome)
        this.scuola = scuola
    }

    get CF() {
        return super.CF + this.scuola;
    }

    get superCF() {
        return super.CF;
    }
}