document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to the month dropdown
    document.getElementById('month-dropdown').addEventListener('change', function() {
        var selectedMonth = this.value;
        
        // Send an AJAX request to fetch data for the selected month
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/fetch-data/?month=' + selectedMonth, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Parse the JSON response
                    var responseData = JSON.parse(xhr.responseText);
                    
                    // Update the displayed content with the fetched data
                    document.getElementById('expenses-container').innerHTML = responseData.expensesHtml;
                    document.getElementById('incomes-container').innerHTML = responseData.incomesHtml;
                } else {
                    // Handle error
                    console.error('Failed to fetch data: ' + xhr.status);
                }
            }
        };
        xhr.send();
    });
});
