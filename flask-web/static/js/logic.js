// function enables theme toggling
function changeTheme(event) {
    const root = $(':root');
    const toggle = $('#toggle');
    if (root.css('--mov_color') == 'rgb(99, 99, 236)') {
         root.css('--mov_color', 'rgb(123, 123, 223)');
         root.css('--bg-color', 'rgb(40, 40, 74)');
         root.css('--txt-color', 'rgb(255, 255, 255)');
         root.css('--task-color', 'rgb(51, 51, 92)');
         root.css('--sub-task-color', 'rgba(255, 255, 255, 0.41)');
         root.css('--box-shadow', '2px 2px 2px rgba(0, 0, 0, 0.387)');
         root.css('--sidebar-border', '1px solid rgba(242, 237, 237, 0.12)');
         root.css('--column-color', 'rgb(69, 69, 106)')
         toggle.addClass('fa-toggle-on').removeClass('fa-toggle-off');
    }
    else {
        root.css('--mov_color', 'rgb(99, 99, 236)');
        root.css('--bg-color', 'rgb(227, 247, 246)');
        root.css('--txt-color', 'black');
        root.css('--task-color', 'white');
        root.css('--sub-task-color', 'rgba(0, 0, 0, 0.387)');
        root.css('--box-shadow', '3px 3px 2px #aaaaaaa0');
        root.css('--sidebar-border', '1px solid rgba(242, 237, 237, 0.571)');
        root.css('--column-color', 'rgb(216, 237, 236)');
        toggle.addClass('fa-toggle-off').removeClass('fa-toggle-on');
    }
}


/*
class Board {
    constructor(name = null, ob = null) {
        this.boardName = name;
        this.Allcolumns = [];
        if (ob !== null) {
            this.boardName = ob.boardName;
            this.Allcolumns = ob.Allcolumns;
        }
        
    }

    getColumns() {
        // return all columns of this board

    }

    createColumn(columnname) {
        // create a column for this board
        const column_obj = {};
        column_obj['colName'] = columnname;
        column_obj['tasks'] = [];
        this.Allcolumns.push(column_obj);
    }

    createTask(columnname, taskName, descrip) {
        // create a task for a particular column
        const ob = {taskName, des: descrip};
        for (let obj of this.Allcolumns) {
            if (columnname == obj['colName']) {
                obj['tasks'].push(ob);
            }
        }
    }

    getTasks(column) {
        // get all tasks in particular column
    }

    createSubTask(taskName, ColumnName, subtask = {subName: '', stat: ''}) {
        // create sub tasks for a particular task
        const sub = subtask;
        for (const obj of this.Allcolumns) {
            if (obj['colName'] === ColumnName) {
                for (const task of obj['tasks']) {
                    if (task['taskName'] === taskName) {
                        if (!task.hasOwnProperty('subtasks')) task['subtasks'] = [];
                        task['subtasks'].push(sub);
                    }
                }
            }
        } 
    }

    getSubTasks(task) {
        // return subtasks for a particular task
    }
}
*/


// create a board
async function createBoard () {
    const boardName = $('#boardName').val();
    console.log(boardName);
    try{
	const res = await $.post('/createBoard', {
	    name: boardName
	});
	console.log(res);
	window.location.href = '/boards/' + res.name;
    } catch(e) {
	console.log(e.responseJSON);
    }
}

function createColumn () {
    const column = $('<aside class="task_aside1 task_aside-item"></aside>').append('<p><i class="fa fa-circle" aria-hidden="true"></i> Todo (4)</p>');
    $('.task_aside').prepend(column);
}

// hide show sidebar
function hideSidebar() {
    $('.side_bar').css('display', 'none');
    $('.showbar').css('display', 'block');
}

// show sidebar
function showSidebar() {
    $('.side_bar').css('display', 'block');
    $('.showbar').css('display', 'none');
}


// toggles the theme between dark and light mode
$('.fa-toggle-on, .fa-toggle-off').click(changeTheme);

// attach an event listener to the hide sidebar icon
$('#hide').click(hideSidebar);

// attach an event listener to show the sidebar
$('#show').click(showSidebar);

// create the board
$('#createBoard').click(createBoard);

// create a column
$('#create_column').click(createColumn);
