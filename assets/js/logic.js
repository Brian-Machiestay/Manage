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

class Board {
    constructor(name = null) {
        this.boadName = name;
        this.Allcolumns = [];
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

    toString() {
        // convert this board to a string
    }
}


class Storage {
    allObjs = [];

    constructor () {

    }

    getBoards() {
        // return all Board instances from storage
    }

    new() {
        // add a new item to storage
    }

    save() {
        // save all board instances to storage
    }

    reload () {
        // get board from storage and return instances
    }
}

// create a board
function createName () {
    $('.board_name').css('display', 'flex');
}
function createColumn () {
    const column = $('<aside class="task_aside1 task_aside-item"></aside>').append('<p><i class="fa fa-circle" aria-hidden="true"></i> Todo (4)</p>');
    $('.task_aside').prepend(column);
}
function createBoard () {
    $('.board_name').css('display', 'none');
    const name = $('.board_name_input').val();
    if (name !== 'Enter board name') {
        $('.logo_item2').text(name);
        $('.task_aside-item').remove();
        $('.create_board').before(`<li href="#" class="list-group-item boardlinks">${name}</li>`);
    }
}


// hide show sidebar
function hideSidebar() {
    $('.side_bar').css('display', 'none');
    $('.showbar').css('display', 'block');
}

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

// listen for board name entry
$('.create_board').click(createName);

// create the board
$('.fa-plus-square-o').click(createBoard);

// create a column
$('#create_column').click(createColumn);

// test cases
board = new Board('Manage app');
board.createColumn('In progress');
board.createTask('In progress', 'Doing the right things at the right time', 'we have been doing this all along');
board.createSubTask('Doing the right things at the right time', 'In progress', {subName: 'doing it right', stat: 'done',})
console.log(board);