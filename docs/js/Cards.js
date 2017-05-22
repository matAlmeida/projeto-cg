function cria_cards(name, description, tipo) {
    let pessoas = document.querySelector(`#${tipo}`);
    let div = document.createElement("div");

    let template = `   
    <a href="#modal1"> 
    <div class="col m6">
        <div class="card hoverable red waves-effect">
            <div class="row valign-wrapper">
                <div class="card-content white-text">
                    <span class="card-title truncate">${name}</span>
                    <p class="truncate">${description}.</p>
                </div>
            </div>
        </div>
    </div>
    </a>
    `;

    div.innerHTML = template;

    pessoas.appendChild(div);
}

function loadCards(pessoas, tipo, clean = false) {
    if (tipo == "pessoas")
        for (let i = 0; i < pessoas.length; i++) {
            let title = StringHelper.titlePessoas(pessoas[i]);
            let description = StringHelper.descriptionPessoas(pessoas[i]);

            cria_cards(title, description, tipo);
        }
    else if (tipo == "donations")
        for (let i = 0; i < pessoas.length; i++) {
            let title = StringHelper.titleDoacao(pessoas[i]);
            let description = StringHelper.descriptionDoacao(pessoas[i]);

            cria_cards(title, description, tipo);
        }
}