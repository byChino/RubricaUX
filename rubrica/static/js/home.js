function filterRubrics() {
    var input = document.getElementById('rubric-search');
    var filter = input.value.toLowerCase();
    var cards = document.getElementById('rubric-cards').getElementsByClassName('rubric-card');
    
    for (var i = 0; i < cards.length; i++) {
        var name = cards[i].getAttribute('data-name').toLowerCase();
        if (name.includes(filter)) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}
