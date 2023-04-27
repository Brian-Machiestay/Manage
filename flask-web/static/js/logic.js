// create global variable to hold board data
let boardData = null;


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


// create a new task
async function createTask() {
    boardName = $('.active').text();
    const title = $('.task_title').val();
    console.log(title);
    const des = $('.task_des').val();
    const item = $('#create_task_status').find(':selected').val();
    const taskOb = {
	boardName: boardName,
	item: item,
	task_title: title.trim(),
	des: des.trim(),
    }
    const sub = []
    for (let i of $('.create_sub_tasksop')) {
	const val = $(i).val();
	if (val.trim() !== '') sub.push(val.trim());
    }
    taskOb.subtasks = JSON.stringify(sub);

    try{
	const res = await $.post('/api/createTask', taskOb);
	console.log(res);
	$('.createTaskInfoma').text('task created successfully');
	$('.createTaskInfoma').addClass('success');
	$('.createTaskInfoma').removeClass('danger');
	setTimeout(() => {
	    $('.createTaskInfoma').text('');
	}, 5000);
    } catch (e) {
	console.log(e);
	$('.createTaskInfoma').text(e.responseJSON.error);
	$('.createTaskInfoma').addClass('danger');
	$('.createTaskInfoma').removeClass('success');
	setTimeout(() => {
	    $('.createTaskInfoma').text('');
	}, 5000);
    }
    console.log(taskOb);
}


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
	$('.createBoardInfo').text(e.responseJSON.error);
	$('.createBoardInfo').addClass('danger');
	$('.createBoardInfo').removeClass('success');
	setTimeout(() => {
	    $('.createBoardInfo').text('');
	}, 5000);
    }
}

// view a task
function viewTask(e) {
    const task_id = e.currentTarget.id;
    const item_id = $(`#${task_id}`).parent().attr('id');
    const task = boardData[item_id]['tasks'][task_id];
    console.log(boardData[item_id]['tasks'][task_id]);
    $('.taskTitle').text(task.title);
    $('.task_description').text(task.des);
    for (const key of Object.keys(task['subtasks'])) {
	console.log(key)
	if (task['subtasks'][key]['status'] === 'checked') {
	    $('#modal_sub_tasks').append('<input type="checkbox" id="sub1" checked disabled="disabled">')
	    $('#modal_sub_tasks').append('<p class="subtaskcontent done">Research competitor pricing and business models</p><br>')
	}
	else {
	    $('#modal_sub_tasks').append('<input type="checkbox" id="sub1" disabled="disabled">')
	    $('#modal_sub_tasks').append('<p class="subtaskcontent">Research competitor pricing and business models</p><br>')
	}
    }
    $('.statusInfo').text(boardData[item_id]['name']);
}



// create a new column
async function createColumn () {
    const colName = $('#colName').val();
    const boardname = $('.active').text();
    console.log(`board name: ${boardname}`);
    console.log(`column name: ${colName}`);
    try{
	const res = await $.post('/api/createColumn', {
	    board: boardname,
	    name: colName,
	});
	console.log(res);
	const column = $('<aside class="task_aside1 task_aside-item"></aside>').append(`<p><i class="fa fa-circle" aria-hidden="true"></i> ${colName} (0)</p>`);
	column.insertBefore('#create_column');
	$('.createColumnInfo').text('column created successfully');
	$('.createColumnInfo').addClass('success');
	$('.createColumnInfo').removeClass('danger');
	$('#create_task_status').append(`<option>${colName}</option>`)
	setTimeout(() => {
	    $('.createColumnInfo').text('');
	}, 5000);
    } catch(e) {
	console.log(e);
	$('.createColumnInfo').text(e.responseJSON.error);
	$('.createColumnInfo').addClass('danger');
	$('.createColumnInfo').removeClass('success');
	setTimeout(() => {
	    $('.createColumnInfo').text('');
	}, 5000);
    }
}

// get the board data from the backend
async function get_board_data() {
    const boardname = $('.active').text();
    const res = await $.post('/api/board_data', {
	board: boardname,
    });
    return res;
}



// add a subtask
function addSubTask() {
    $('#create_sub_tasks').append('<input type="text" class="create_sub_tasksop" value=""> <i class="fa fa-times removeTask" aria-hidden="true"></i><br>');
    $('.removeTask').click(removeSubTask);
}

// remove a subtask
function removeSubTask(e) {
    $(e.target).prev().remove();
    $(e.target).next().remove();
    $(e.target).remove();
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


// load the current's board data
get_board_data().then((res) => {
    boardData = res;
    console.log(boardData);
});

// toggles the theme between dark and light mode
$('.fa-toggle-on, .fa-toggle-off').click(changeTheme);

// attach an event listener to the hide sidebar icon
$('#hide').click(hideSidebar);

// attach an event listener to show the sidebar
$('#show').click(showSidebar);

// create the board
$('#createBoard').click(createBoard);

// create a column
$('#createColumn').click(createColumn);


// add a subtask
$('.add_sub_task').click(addSubTask);

// remove subtask
$('.removeTask').click(removeSubTask);

// create a task
$('.create_task').click(createTask);

// listen on task click
$('.task').click(viewTask);
