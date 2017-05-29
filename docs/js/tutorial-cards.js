function createTutoCard(tutorialNumber, tutorialTitle, tutorialLink, tutorialLibs, tutorialDescription) {

    let panel = document.querySelector("#cards-tuto");

    let div = document.createElement("div");
    div.classList.add("card");
    div.classList.add("hoverable");
    div.classList.add("col");
    div.classList.add("m4");

    div.innerHTML = `
    <div class="card-image waves-effect waves-block waves-light">
        <img class="activator" src="images/tutorial-${tutorialNumber}.png">
    </div>
    <div class="card-content">
        <span class="card-title activator grey-text text-darken-4 truncate">Tutorial ${tutorialNumber}<i class="material-icons right">more_vert</i></span>
        <p class="truncate"><a href="${tutorialLink}" target="_blank">${tutorialTitle}</a></p>
    </div>
    <div class="card-reveal">
        <span class="card-title grey-text text-darken-4">Bibliotecas utilizadas<i class="material-icons right">close</i></span>
        <p>${tutorialLibs}</p>
        <span class="card-title grey-text text-darken-4">Descrição</span>
        <p>${tutorialDescription}</p>
    </div>
    `;

    panel.appendChild(div);
}

function genTutoCards(tutos) {

    tutos.forEach(function(element) {
        createTutoCard(element["Numero"], element["Titulo"], element["Link"], element["Bibliotecas"], element["Descricao"]);
    }, this);

    // document.querySelector("#progressBar").innerHTML = "";
}