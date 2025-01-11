(function() {

    function iidxlayout(axis) {

        var map = {
            left:  axis == 'left' || axis == 'center_left' ? 'left'  : 'right',
            right: axis == 'left' || axis == 'center_left' ? 'right' : 'left'
        };

        function x(index) {
            if(axis == 'center_left' || axis == 'center_right')
                return window.innerWidth / 2 - 310 + 100 * index; // Increased spacing
            return 310 + 85 * index;
        }

        function y(index) {
            if (axis == 'center_left' || axis == 'center_right')
                return window.innerHeight / 2 - 245 + 300 * (index % 2);
            return 0 + 245 * (index % 2);
        }

        function style(index) {
            var style = {
                bottom: y(index) + 'px',
                width: (axis == 'center_left' || axis == 'center_right') ? '150px' : '120px',
                height: (axis == 'center_left' || axis == 'center_right') ? '250px' : '200px'
            };
            style[map.left] = x(index) + 'px';
            return style;
        }

        return function(ui) {
            ui.button('iidx_1', style(0));
            ui.button('iidx_2', style(1));
            ui.button('iidx_3', style(2));
            ui.button('iidx_4', style(3));
            ui.button('iidx_5', style(4));
            ui.button('iidx_6', style(5));
            ui.button('iidx_7', style(6));
            ui.turntable((axis == 'center_left' || axis == 'center_right') ? '280px' : '220px', map.left);
        };

    }

    i2DX.layout('iidx_left', iidxlayout('left'));
    i2DX.layout('iidx_right', iidxlayout('right'));
    i2DX.layout('iidx_center_left', iidxlayout('center_left'));
    i2DX.layout('iidx_center_right', iidxlayout('center_right'));

    i2DX.layout('turntable', function(ui) {
        ui.turntableFullscreen();
    });

})();