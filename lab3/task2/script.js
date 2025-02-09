function addTask() {
    let task = document.getElementById('new-task');
    const table = document.querySelector("table");
    // Создаём новый элемент <tr> при каждом вызове
    let newTask = document.createElement("tr");
    
    newTask.innerHTML = `
    <td>
        <div class="task">
            <input class="font task-inner" type="checkbox" name="task">
            <p class="task-text font task-inner"> ${task.value}</p>
            <img class="delete-task task-inner" src="images/trash_can.png" alt="Delete"> 
        </div>
    </td>`;
    
    table.appendChild(newTask);
    task.value = "";

    const checkbox = newTask.querySelector(".task input");
    const textElement = newTask.querySelector(".task-text");

    checkbox.addEventListener("change", function () {
        if (this.checked) {
            textElement.style.textDecoration = "line-through";
        } else {
            textElement.style.textDecoration = "none";
        }
    });

    const deleteButton = newTask.querySelector(".delete-task");
    deleteButton.addEventListener("click", function () {
        newTask.remove(); // Удаляем всю строку <tr>
    });
}
