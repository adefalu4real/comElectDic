// scripts.js
function searchTerm() {
    var searchQuery = document.getElementById('search').value;
    fetch('/search?term=' + searchQuery)
        .then((response) => response.json())
        .then(data => {
            var resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';
            data.forEach(item => {
                var termDiv = document.createElement('div');
                termDiv.className = 'term';
                termDiv.innerHTML = '<h2>' + item.word + '</h2>';
                item.meanings.forEach(meaning => {
                    meaning.definitions.forEach(def => {
                        termDiv.innerHTML += '<p>' + def.definition + '</p>';
                        if (def.example) {
                            termDiv.innerHTML += '<p><em>Example: ' + def.example + '</em></p>';
                        }
                        if (def.image_url) {
                            termDiv.innerHTML += '<img src="' + def.image_url + '" alt="' + item.word + '">';
                        }
                    });
                });
                resultsDiv.appendChild(termDiv);
            });
        })
        .catch(error => {
            console.error('Error fetching the term:', error);
        });
}

function checkEnter(event) {
    if (event.key === 'Enter') {
        searchTerm();
    }
}
