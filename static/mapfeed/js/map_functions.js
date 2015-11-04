function pulsate(element) {
    $(element || this).animate({ opacity: 0 }, 1000, function() {
        $(this).animate({ opacity: 0.75 }, 1000,  pulsate);
    });
}

function drawLine(x1, y1, x2, y2, num_lines, order, lineweight) {
    var delta_x = x2 - x1;
    var delta_y = y2 - y1;
    var slope = delta_y / delta_x;

    if (delta_x == 0) {
        var offset_x = 1;
        var offset_y = 1;
    } else if (slope > 0) {
        var offset_x = 1;
        var offset_y = 0;
    } else if (slope <= 0) {
        var offset_x = 0;
        var offset_y = 1;
    }

    switch(num_lines){
        case 1:
            line(x1, y1, x2, y2);
            break;
        case 2:
            if(order == 1)
                line(x1 + offset_x * lineweight, y1 + offset_y * lineweight, x2 + offset_x * lineweight, y2 + offset_y * lineweight);
            else if(order == 2)
                line(x1 - offset_x * lineweight, y1 - offset_y * lineweight, x2 - offset_x * lineweight, y2 - offset_y * lineweight);
            break;
        case 3:
            if(order == 1)
                line(x1, y1, x2, y2);
            else if(order == 2)
                line(x1 + offset_x * lineweight * 1.3, y1 + offset_y * lineweight * 1.3, x2 + offset_x * lineweight * 1.3, y2 + offset_y * lineweight * 1.3);
            else if(order == 3)
                line(x1 - offset_x * lineweight * 1.3, y1 - offset_y * lineweight * 1.3, x2 - offset_x * lineweight * 1.3, y2 - offset_y * lineweight * 1.3);
            break;
    }
}

pulsate("#alerts");
