var hidden_timer = 8000;

notification = {
    primary: function (message, from, align) {
        $.notify({
            icon: "tim-icons icon-bell-55",
            message: message
        }, {
            type: 'primary',
            timer: hidden_timer,
            placement: {from: from, align: align}
        });
    },
    info: function (message, from, align) {
        $.notify({
            icon: "tim-icons icon-bell-55",
            message: message
        }, {
            type: 'info',
            timer: hidden_timer,
            placement: {from: from, align: align}
        });
    },
    success: function (message, from, align) {
        $.notify({
            icon: "tim-icons icon-bell-55",
            message: message
        }, {
            type: 'success',
            timer: hidden_timer,
            placement: {from: from, align: align}
        });
    },
    warning: function (message, from, align) {
        $.notify({
            icon: "tim-icons icon-bell-55",
            message: message
        }, {
            type: 'warning',
            timer: hidden_timer,
            placement: {from: from, align: align}
        });
    },
    danger: function (message, from, align) {
        $.notify({
            icon: "tim-icons icon-bell-55",
            message: message
        }, {
            type: 'danger',
            timer: hidden_timer,
            placement: {from: from, align: align}
        });
    }
};

$(document).ready(function () {

    $('.custom-file-input').on('change',function(){
        var fileName = $(this).val().replace(/C:\\fakepath\\/i, '');
        $(this).parent().find('label').text(fileName);
    })
    $().ready(function () {
        $sidebar = $('.sidebar');
        $navbar = $('.navbar');
        $main_panel = $('.main-panel');
        $full_page = $('.full-page');
        $sidebar_responsive = $('body > .navbar-collapse');
        sidebar_mini_active = true;
        white_color = false;
        window_width = $(window).width();
        fixed_plugin_open = $('.sidebar .sidebar-wrapper .nav li.active a p').html();

        $('.fixed-plugin a').click(function (event) {
            if ($(this).hasClass('switch-trigger')) {
                if (event.stopPropagation) {
                    event.stopPropagation();
                } else if (window.event) {
                    window.event.cancelBubble = true;
                }
            }
        });

        var new_color = $('.fixed-plugin .background-color span.active').data('color');
        // change sidebar background
        ChangeSidBarBackground(new_color);

        $('.fixed-plugin .background-color span').click(function () {
            $(this).siblings().removeClass('active');
            $(this).addClass('active');
            new_color = $(this).data('color');

            // change sidebar background
            ChangeSidBarBackground(new_color);

            // update dashboard setting
            AjaxUpdateAdminBlackSetting({'sidebar_background': new_color});
        });

        $('.switch-sidebar-mini input').on("switchChange.bootstrapSwitch", function () {
            var $btn = $(this);
            if (sidebar_mini_active == true) {
                $('body').removeClass('sidebar-mini');
                sidebar_mini_active = false;
                blackDashboard.showSidebarMessage('Sidebar mini deactivated...');
            } else {
                $('body').addClass('sidebar-mini');
                sidebar_mini_active = true;
                blackDashboard.showSidebarMessage('Sidebar mini activated...');
            }

            // we simulate the window Resize so the charts will get updated in realtime.
            var simulateWindowResize = setInterval(function () {
                window.dispatchEvent(new Event('resize'));
            }, 180);

            // we stop the simulation of Window Resize after the animations are completed
            setTimeout(function () {
                clearInterval(simulateWindowResize);
            }, 1000);
        });

        $('.switch-change-color input').on("switchChange.bootstrapSwitch", function () {
            var $btn = $(this);

            if (white_color == true) {

                $('body').addClass('change-background');
                setTimeout(function () {
                    $('body').removeClass('change-background');
                    $('body').removeClass('white-content');
                }, 900);
                white_color = false;
            } else {

                $('body').addClass('change-background');
                setTimeout(function () {
                    $('body').removeClass('change-background');
                    $('body').addClass('white-content');
                }, 900);

                white_color = true;
            }


        });

        $('.light-badge').click(function () {
            $('body').addClass('white-content');
            $('select').attr('style', 'background-color:#ffffff;');
            // update dashboard setting
            AjaxUpdateAdminBlackSetting({'dark_mode': 0});
        });
        $('.dark-badge').click(function () {
            $('body').removeClass('white-content');
            $('select').attr('style', 'background-color:#27293c;');
            // update dashboard setting
            AjaxUpdateAdminBlackSetting({'dark_mode': 1});
        });
    });

    demo.initDashboardPageCharts();

    window.TrackJS &&
    TrackJS.install({
        token: "ee6fab19c5a04ac1a32a645abde4613a",
        application: "black-dashboard-free"
    });
});

function ChangeSidBarBackground(new_color) {
    $sidebar = $('.sidebar');
    $main_panel = $('.main-panel');
    $full_page = $('.full-page');
    $sidebar_responsive = $('body > .navbar-collapse');

    if ($sidebar.length != 0)
        $sidebar.attr('data', new_color);
    if ($main_panel.length != 0)
        $main_panel.attr('data', new_color);
    if ($full_page.length != 0)
        $full_page.attr('filter-color', new_color);
    if ($sidebar_responsive.length != 0)
        $sidebar_responsive.attr('data', new_color);
}

function AjaxUpdateAdminBlackSetting(form_data) {
    var setting_url = $('#AdminBlackSetting').data('url');

    $.ajax({
        url: setting_url,
        type: 'POST',
        data: form_data,
        success: function (data) {
//            console.log(data);
            console.log('');
        },
        error: function () {
            alert('Error occurred');
        }
    });
}

/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
//var dropdown = document.getElementsByClassName("navbar-btn");
//var i;
//
//for (i = 0; i < dropdown.length; i++) {
//    dropdown[i].addEventListener("click", function () {
//        this.classList.toggle("active");
//        var dropdownContent = this.nextElementSibling;
//        if (dropdownContent.style.display === "block") {
//            dropdownContent.style.display = "none";
//        } else {
//            dropdownContent.style.display = "block";
//        }
//    });
//}

//Added by robin
$(document).ready(function () {
    $sidebar = $('.sidebar');
    $sidebar.on('click', 'a.navbar-btn', function() {
        $this = $(this);
        makeURLActive($this);
    });
    $selectedLi = $sidebar.find('.selected');
    if($selectedLi.length > 0) {
        makeURLActive($selectedLi.closest('ul.navbar-dropdown').parent().find('a.navbar-btn'));
    }

    function makeURLActive($this)
    {
        $icon = $this.find('.m-2');
        if($this.hasClass('active')) {
            $this.removeClass('active');
            $icon.addClass('m-2-90');
            $this.parent().find('ul.navbar-dropdown').slideUp();
        } else {
            $this.addClass('active');
            $icon.removeClass('m-2-90');
            $this.parent().find('ul.navbar-dropdown').slideDown();
        }
    }

    $('body').on('click', '.sendmailbutton', function() {
        var $this = $(this);
        var $parent = $this.parent();
        var url = $this.attr('href');
        $parent.html('<i class="tim-icons icon-refresh-01"></i>');
        notification.warning("<p class='text-left'>Sending email.</p>", 'top', "right");
        $.ajax({
            url: url,
            async: true,
            contentType: "application/json; charset=utf-8",
            success: function (data) {
              if(data.status == 200) {
                $parent.parent().html(data.email_no + ' <i class="tim-icons icon-check-2"></i>');
                notification.success("<p class='" + data.panel + "'>" + data.message + "</p>", 'top', data.notify);
              } else {
                $parent.html('<i class="tim-icons icon-simple-remove"></i>');
                notification.danger("<p class='" + data.panel + "'>" + data.message + "</p>", 'top', data.notify);
              }
            },
            error: function(xhr, error) {
                $parent.html('<i class="tim-icons icon-simple-remove"></i>');
                notification.danger("<p class='text-left'>Error while sending email. Please try later</p>", 'top', "right");
            }
          });
        return false;
    })
});