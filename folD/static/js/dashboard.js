document.addEventListener('DOMContentLoaded', function () {
    // Function to make an AJAX request for expenses and income data
    function fetchData(month) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/fetch-data/?month=' + month, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Parse the JSON response
                    var responseData = JSON.parse(xhr.responseText);
                    
                    // Update the expenses, total income, and balance based on fetched data
                    updateExpensesTotalIncomeAndBalance(responseData);
                } else {
                    // Handle error
                    console.error('Failed to fetch data: ' + xhr.status);
                }
            }
        };
        xhr.send();
    }

    // Function to update the expenses, total income, and balance based on fetched data
    function updateExpensesTotalIncomeAndBalance(data) {
        var expensesContainer = document.getElementById('expenses-container');
        expensesContainer.innerHTML = ''; // Clear existing content
        
        // Calculate total expenses
        var totalExpenses = data.expenses.reduce((total, expense) => total + parseFloat(expense.amount), 0);
        totalExpenses = '$' + totalExpenses.toFixed(2);

        // Update the expenses tab with the fetched data
        data.expenses.forEach(function(expense) {
            var expenseItem = document.createElement('div');
            expenseItem.classList.add('DAS_expenses_data_item');
            expenseItem.innerHTML = '<li>' + expense.place + '</li><li>-$' + expense.amount + '</li>';
            expensesContainer.appendChild(expenseItem);
        });

        // Display total expenses
        var expensesTotalElement = document.getElementById('expenses-total');
        expensesTotalElement.textContent = totalExpenses;

        // Display total income
        var totalIncomeElement = document.getElementById('total-income');
        totalIncomeElement.textContent = '$' + data.total_income.toFixed(2);

        // Calculate balance
        var balance = data.total_income - parseFloat(totalExpenses);

        // Display balance
        var balanceElement = document.getElementById('balance');
        balanceElement.textContent = '$' + balance.toFixed(2);
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
        fetchData(selectedMonth);
    });

    // Make an initial AJAX request for expenses and income data of the current month
    fetchData(currentMonthYear);
});
