function changeTheme(event) {
    console.log($(":root").css('--mov_color'));
    console.log($(':root').style.getPropertyValue('--mov_color'));
    if ($(':root').css('--mov_color') == 'rgb(99, 99, 236)') $(':root').css('--mov_color');
    else $(':root').attr('--mov_color', 'rgb(99, 99, 236)')
}

$('.fa-toggle-on').click(changeTheme);