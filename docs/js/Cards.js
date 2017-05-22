function cria_cards(name, description, tipo) {
    let pessoas = document.querySelector(`#${tipo}`);
    let div = document.createElement("div");
    div.classList.add("teste");
    let color = 'red';
    if (tipo == "donations4me")
        color = 'green';

    let template = `   
    <a href="#modal1"> 
    <div class="col m6">
        <div class="card hoverable ${color} waves-effect">
            <div class="row valign-wrapper">
                <div class="col s2">
                    <img src="res/logo.svg" alt="" class="circle responsive-img"> <!-- notice the "circle" class -->
                </div>
                <div class="card-content white-text col s10">
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