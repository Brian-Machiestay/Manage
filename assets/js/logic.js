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

// create a board
function createName () {
    $('.board_name').css('display', 'flex');
}
function createColumn () {
    const column = $('<aside class="task_aside1 task_aside-item"></aside>').append('<p><i class="fa fa-circle" aria-hidden="true"></i> Todo (4)</p>');
    $('.task_aside').after(column);
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