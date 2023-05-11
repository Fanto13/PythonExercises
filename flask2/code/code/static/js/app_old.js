var carrello = [];
//questa funzione serve per prendere il valore del campo di testo, lo trimma e lo ritorna se è valido, altrimenti ritorna undefined
function validateInput(x) {
    trimmed = x.trim();
    if (trimmed.length <= 0)
        return undefined;
    return trimmed;
}
//questa funzione serve per aggiungere un prodotto al carrello
function addProduct() {
    event.preventDefault(); // submit del form

    let nome = validateInput(prodottoTXT.value);
    if (nome == undefined) {
        alert("Nome prodotto non valido!");
        return;
    }
//se il prodotto è già presente nel carrello, incrementa la quantità, altrimenti lo aggiunge
    let filtrato = carrello.filter(x => x.nome == nome);
    if (filtrato.length > 0) {
        increaseQuantity(filtrato);
    } else {
        addNewProduct(nome);
    }
    stampa();
}
//un sample di prodotto è {nome: "prodotto", prezzo: 10, quantita: 1}
function addNewProduct(nome) {
    let prodotto = {
        nome: nome,
        prezzo: 10,
        quantita: 1
    };
    carrello.push(prodotto);
}

function increaseQuantity(filtrato) {
    filtrato[0].quantita++;

    // copia = filtrato[0];
    // idx = carrello.indexOf(copia);
    // carrello[idx].quantita++;
}

function removeProduct(daRimuovere) {
    idx = -1;//questo è un valore di default, se non trova il prodotto da rimuovere, rimane -1
    for (let i = 0; i < carrello.length; i++) {
        if (carrello[i].nome == daRimuovere)
            idx = i;//metto l'indice del prodotto da rimuovere
    }
    carrello.splice(idx, 1);
    stampa();
}
//sottrae la quantità di un prodotto, se la quantità è 0, rimuove il prodotto
function subQuantity(daRimuovere) {
    for (let i = 0; i < carrello.length; i++) {
        if (carrello[i].nome == daRimuovere) {//se il prodotto è presente nel carrello, 
            carrello[i].quantita--;
            if (carrello[i].quantita <= 0)
                removeProduct(daRimuovere);
        }
    }
    stampa();
}
//aggiounge la quantità di un prodotto
function addQuantity(daRimuovere) {
    for (let i = 0; i < carrello.length; i++) {
        if (carrello[i].nome == daRimuovere)
            carrello[i].quantita++;
    }
    stampa();
}

function stampa() {
    carrelloUL.innerHTML = "";
    // per ogni prodotto nel carrello, stampa il nome e la quantità
    for (let prodotto of carrello) {
        let item = prodotto.nome;
        // carrelloUL.innerHTML = "<li>" + item + "</li>"
        carrelloUL.innerHTML += /*html*/ `
            <li>${item} - ${prodotto.quantita}
                <button onclick="removeProduct('${item}')">X</button>
                <button onclick="subQuantity('${item}')">-</button>
                <button onclick="addQuantity('${item}')">+</button>
            </li>`;
    }
}