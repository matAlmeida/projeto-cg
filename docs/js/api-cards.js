function createCard(func_name, description, params, retorno, proto, variation) {

    let sectionApi = document.querySelector("#api");

    if (variation != undefined) {
        variation = `
        <li>
            <div class="collapsible-header"><i class="material-icons">transform</i>Variações</div>
            <div class="collapsible-body"><span>${variation}</span></div>
        </li>
        
        `;
    } else {
        variation = "";
    }

    let div = document.createElement("span");
    div.classList.add("red-text");
    div.innerHTML = `
        <ul class="collapsible a-funcoes red-text" data-collapsible="accordion">
            <li>
                <div class="collapsible-header active func-name"><i class="material-icons">description</i>${func_name}</div>
                <div class="collapsible-body"><span>${description}</span></div>
            </li>
            <li>
                <div class="collapsible-header"><i class="material-icons">list</i>Parâmetros / Retorno</div>
                <div class="collapsible-body"><span>
                    <strong>Parâmetros</strong><br>
                    <p style="margin-left: 25px">${params}</p>
                    <strong>Retorno</strong><br>
                    <p style="margin-left: 25px">${retorno}</p>
                </span></div>
            </li>
            <li>
                <div class="collapsible-header"><i class="material-icons">fingerprint</i>Prótotipo</div>
                <div class="collapsible-body"><span>${proto}</span></div>
            </li>
            ${variation}
        </ul>
    `;

    sectionApi.appendChild(div);
}

function genCards(functions) {
    functions.forEach(function(element) {
        createCard(element["Função"], element["Descrição"], element["Parâmetros"], element["Retorno"], element["Protótipo"], element["Variações da Função"]);
    }, this);

    document.querySelector("#progressBar").innerHTML = "";
}