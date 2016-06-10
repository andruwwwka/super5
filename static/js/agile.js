function changePriority() {
    for (var a=[], i=document.getElementsByClassName('draggable').length; i;)
        a[--i] = document.getElementsByClassName('draggable')[i].id;

	$.ajax({
            type: 'get',
            url: 'change_priority/',
            data: {'data': a.join(';') }
        });
}
