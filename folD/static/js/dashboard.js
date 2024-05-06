document.addEventListener('DOMContentLoaded', function () {
    // Function to make an AJAX request for expenses data
    function fetchExpensesData(month) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/fetch-data/?month=' + month, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Parse the JSON response
                    var responseData = JSON.parse(xhr.responseText);
                    
                    // Update the expenses tab with the fetched data
                    updateExpensesTab(responseData);
                } else {
                    // Handle error
                    console.error('Failed to fetch data: ' + xhr.status);
                }
            }
        };
        xhr.send();
    }

    // Function to update the expenses tab with fetched data
    function updateExpensesTab(data) {
        var expensesContainer = document.getElementById('expenses-container');
        expensesContainer.innerHTML = ''; // Clear existing content
        
        // Iterate over the expenses data and create HTML elements
        data.expenses.forEach(function(expense) {
            var expenseItem = document.createElement('div');
            expenseItem.classList.add('DAS_expenses_data_item');
            expenseItem.innerHTML = '<li>' + expense.place + '</li><li>-$' + expense.amount + '</li>';
            expensesContainer.appendChild(expenseItem);
        });
    }

    // Get the current month and year
    var currentMonth = new Date().toLocaleString('default', { month: 'long' });
    var currentYear = new Date().getFullYear();
    var currentMonthYear = currentMonth + ' ' + currentYear;

    // Add event listener to the month dropdown
    var monthDropdown = document.getElementById('month-dropdown');
    monthDropdown.addEventListener('change', function() {
        var selectedMonth = this.value;
        
        // Send an AJAX request to fetch data for the selected month
        fetchExpensesData(selectedMonth);
    });

    // Make an initial AJAX request for expenses data of the current month
    fetchExpensesData(currentMonthYear);
});