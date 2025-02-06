//  Adopted from Terje
// Model
    let tasks = [
        { description: 'Handle til middag', 
            isDone: true, 
            deadline:"", 
            timestamp:"", 
            assigned:""  },
    ];

    let team = 
    [
        {CEO:["Jhon Doe"]},
        {teamleader:["Jane Doe"]},
        {employee:["Jim Doe"]} ,
    ]

    // Controller

    function addTask() 
    {

        //  Initializing tasks description input
        
        let date = document.getElementById("date");
        let input = document.getElementById('taskDescription');
        let assign = document.getElementById('employee');

        //  Pushing input value
        console.log(new Date(), date.value)
        tasks.push({
            description: input.value,
            isDone: false,
            deadline:date.value,
            assigned:assign.value,
            timestamp:""});

        input.value = '';

        show();
    }

    function FormElement()
    {
        let employee = team[2].employee;
        let select = document.getElementById('employee');
        html = "";
        

        for (let i = 0; i < employee.length; i++)
        {
            if (employee[i])
                console.log(employee[i])
            {
                html += /*HTML*/`<option value="${employee[i]}">${employee[i]}</option>`;
            }
        }
    
        select.innerHTML = html;
    }

    show();
// View
    function show() 
    {
        let tasksTable = document.getElementById("task-wrapper");

        let html = /*HTML*/`
                        <tr>
                            <th>Oppgave</th>
                            <th>Done</th>
                            <th></th>
                            <th>asigned to</th>
                            <th>Deadline</th>
                            <th>TimerStamp</th>
                            <th></th>

                        </tr>`;

        for (let i = 0; i < tasks.length; i++) {
            html += createHtmlRow(i);
        }
        tasksTable.innerHTML = html;
        FormElement();

        return;
    }
    
    function createHtmlRow(i) 
    {

        const task = tasks[i];
        const checkedHtml = task.isDone ? 'checked="checked"' : '';

        if (!task.editMode)
            return /*HTML*/`<tr>
                            <td>${task.description}</td>
                            <td><input onchange="changeIsDone(this, ${i})" type="checkbox" ${checkedHtml} /></td>
                            <td>
                                <button onclick="deleteTask(${i})">Slett</button>
                                <button onclick="editTask(${i})">Rediger</button>
                            </td>
                            <td>${task.assigned}</td>
                            <td>${task.deadline}</td>
                            <td>${task.timestamp}</td>
                        </tr>`;
        return /*HTML*/`<tr>
                            <td><input id="editDescription${i}" type="text" value="${task.description}"/></td>
                            <td><input onchange="changeIsDone(this, ${i})" type="checkbox" ${checkedHtml} /></td>
                            <td>
                                <button onclick="updateTask(${i})">Lagre</button>
                            </td>
                        </tr>
                        `;
    }

    function changeIsDone(checkbox, index) {
        tasks[index].isDone = checkbox.checked;
        timestamp(index);
        show();
    }

    function updateTask(index) {
        const id = `editDescription${index}`;
        const inputTag = document.getElementById(id);
        const task = tasks[index];


        task.description = inputTag.value;
        task.editMode = false;
        show();
    }

//  @krigjo25 

function timestamp(i)
{
    //  Ensure that checked is true
    if (tasks[i].isDone == true)
    {
        tasks[i].timestamp = new Date();
    }
}

    function deleteTask(index) {
        tasks.splice(index, 1);
        show();
    }

    function editTask(index) {
        tasks[index].editMode = true;
        show();
    }
