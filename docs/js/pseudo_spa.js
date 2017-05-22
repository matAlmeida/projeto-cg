function page_load(pageName) {
    let page = document.querySelector("#page1");

    page.innerHTML = ``;

    $("#page1").load(`templates/${pageName}.html`);
}