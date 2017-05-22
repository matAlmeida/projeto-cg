function createCard(func_name, description, params, retorno, proto, variation){

    let sectionApi = document.querySelector("#api");

    if(variation != undefined){
        variation = `
        <li>
            <div class="collapsible-header"><i class="material-icons">transform</i>Variações</div>
            <div class="collapsible-body"><span>${variation}</span></div>
        </li>
        
        `;
    } 
    else
        variation = "";

    let div = document.createElement("div");
    div.classList.add("row");
    div. innerHTML = `
        <div class="col s12">
            <div class="card-panel">
                <span class="red-text">
                    <ul class="collapsible" data-collapsible="accordion">
                        <li>
                            <div class="collapsible-header active"><i class="material-icons">description</i>${func_name}</div>
                            <div class="collapsible-body"><span>${description}</span></div>
                        </li>
                        <li>
                            <div class="collapsible-header"><i class="material-icons">list</i>Parâmetros / Retorno</div>
                            <div class="collapsible-body"><span>
                                <h5 class="header">Parâmetros</h5><br>
                                <p>${params}</p>
                                <h5 class="header">Retorno</h5><br>
                                <p>${retorno}</p>
                            </span></div>
                        </li>
                        <li>
                            <div class="collapsible-header"><i class="material-icons">fingerprint</i>Prótotipo</div>
                            <div class="collapsible-body"><span>${proto}</span></div>
                        </li>
                        ${variation}
                    </ul>
                </span>
            </div>
        </div>
    `;

    sectionApi.appendChild(div);
}

function genCards(functions){
    functions.forEach(function(element) {
        createCard(element["Função"], element["Descrição"], element["Parâmetros"], element["Retorno"], element["Protótipo"], element["Variações da função"]);
    }, this);
}