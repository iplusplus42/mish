global_head = '''
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="stylesheet" href="{a}" />
<link rel="stylesheet" href="{b}" />
<link rel="stylesheet" href="{c}" />
<link rel="stylesheet" href="{d}" />
<link rel="stylesheet" href="{e}" />
<link href="{f}" rel="stylesheet" />
<link rel="stylesheet" href="{g}" />
<link href='http://fonts.googleapis.com/css?family=Open+Sans:400,700,800' rel='stylesheet' type='text/css'>
'''
global_navbar = '''
<div id="user-nav" class="navbar navbar-inverse">
  <ul class="nav">
    <li  class="dropdown" id="profile-messages" ><a title="" href="#" data-toggle="dropdown" data-target="#profile-messages" class="dropdown-toggle"><i class="icon icon-user"></i>  <span class="text">Welcome {a}</span><b class="caret"></b></a>
      <ul class="dropdown-menu">
        <li><a href="#"><i class="icon-user"></i> My Profile</a></li>
        <li class="divider"></li>
        <li><a href="#"><i class="icon-check"></i> My Tasks</a></li>
        <li class="divider"></li>
        <li><a href="login.html"><i class="icon-key"></i> Log Out</a></li>
      </ul>
    </li>
    <li class="dropdown" id="menu-messages"><a href="#" data-toggle="dropdown" data-target="#menu-messages" class="dropdown-toggle"><i class="icon icon-envelope"></i> <span class="text">Messages</span> <span class="label label-important">{b}</span> <b class="caret"></b></a>
      <ul class="dropdown-menu">
        <li><a class="sAdd" title="" href="#"><i class="icon-plus"></i> new message</a></li>
        <li class="divider"></li>
        <li><a class="sInbox" title="" href="#"><i class="icon-envelope"></i> inbox</a></li>
        <li class="divider"></li>
        <li><a class="sOutbox" title="" href="#"><i class="icon-arrow-up"></i> outbox</a></li>
        <li class="divider"></li>
        <li><a class="sTrash" title="" href="#"><i class="icon-trash"></i> trash</a></li>
      </ul>
    </li>
    <li class=""><a title="" href="#"><i class="icon icon-cog"></i> <span class="text">Settings</span></a></li>
    <li class=""><a title="" href="login.html"><i class="icon icon-share-alt"></i> <span class="text">Logout</span></a></li>
  </ul>
</div>
<div id="search">
  <input type="text" placeholder="Search here..."/>
  <button type="submit" class="tip-bottom" title="Search"><i class="icon-search icon-white"></i></button>
</div>
'''
global_sidebar = '''
<div id="sidebar"><a href="#" class="visible-phone"><i class="icon icon-home"></i> Dashboard</a>
  <ul>
    <li class="active"><a href="{a}"><i class="icon icon-home"></i> <span>Dashboard</span></a> </li>
    <li class=""><a href="{b}"><i class="icon icon-signal"></i> <span>Server Analytics (WIP)</span></a> </li>
    <li class=""><a href="{c}"><i class="icon icon-info-sign"></i> <span>Updates</span></a> </li>
    <li class=""><a href="{d}"><i class="icon icon-th-list"></i> <span>Servers</span></a></li>
    <li class=""><a href="{e}"><i class="icon icon-user"></i> <span>Users</span></a></li>
    <li class=""><a href="{f}"><i class="icon icon-th"></i> <span>Addons</span> <span class="label label-important">!</span></a></li>
    <li class="content"> <span>Disk Space Usage</span>
      <div class="progress progress-mini active progress-striped">
        <div style="width: {disk_pct}%;" class="bar"></div>
      </div>
      <span class="percent">{disk_pct}</span>
      <div class="stat">{disk_use}</div>
    </li>
  </ul>
</div>
'''
global_js = '''
<div>
  <script src="{{ url_for('static', filename='js/excanvas.min.js') }}"></script>
  <script src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
  <script src="{{ url_for('static', filename='js/jquery.ui.custom.js') }}"></script>
  <script src="{{ url_for('static', filename='js/bootstrap.min.js') }}"></script>
  <script src="{{ url_for('static', filename='js/jquery.flot.min.js') }}"></script>
  <script src="{{ url_for('static', filename='js/jquery.flot.resize.min.js') }}"></script>
  <script src="{{ url_for('static', filename='js/jquery.peity.min.js') }}"></script>
  <script src="{{ url_for('static', filename='js/fullcalendar.min.js') }}"></script>
  <script src="{{ url_for('static', filename='js/matrix.js') }}"></script>
  <script src="{{ url_for('static', filename='js/matrix.dashboard.js') }}"></script>
  <script src="{{ url_for('static', filename='js/jquery.gritter.min.js') }}"></script>
  <script src="{{ url_for('static', filename='js/matrix.interface.js') }}"></script>
  <script src="{{ url_for('static', filename='js/matrix.chat.js') }}"></script>
  <script src="{{ url_for('static', filename='js/jquery.validate.js') }}"></script>
  <script src="{{ url_for('static', filename='js/matrix.form_validation.js') }}"></script>
  <script src="{{ url_for('static', filename='js/jquery.wizard.js') }}"></script>
  <script src="{{ url_for('static', filename='js/jquery.uniform.js') }}"></script>
  <script src="{{ url_for('static', filename='js/select2.min.js') }}"></script>
  <script src="{{ url_for('static', filename='js/matrix.popover.js') }}"></script>
  <script src="{{ url_for('static', filename='js/jquery.dataTables.min.js') }}"></script>
  <script src="{{ url_for('static', filename='js/matrix.tables.js') }}"></script>

  <script type="text/javascript">
    // This function is called from the pop-up menus to transfer to
    // a different page. Ignore if the value returned is a null string:
    function goPage (newURL) {

        // if url is empty, skip the menu dividers and reset the menu selection to default
        if (newURL != "") {

            // if url is "-", it is this page -- reset the menu:
            if (newURL == "-" ) {
                resetMenu();
            }
            // else, send page to designated URL
            else {
              document.location.href = newURL;
            }
        }
    }

  // resets the menu selection upon entry to this page:
    function resetMenu() {
       document.gomenu.selector.selectedIndex = 2;
    }
  </script>
</div>
'''
