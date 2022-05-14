var levelClass = $('#qmt-manufacturer').find('option:selected').attr('class');
$('#qmt-model option').each(function() {
    var self = $(this);
    self.hide();
    if (self.hasClass(levelClass)) {
       self.show();
    }
 });
 $(function() {
    $("#qmt-vehicle").on("change", function() {
       var levelClass = $('#qmt-vehicle').find('option:selected').attr('class');
       console.log(levelClass);
       $('#qmt-manufacturer option').each(function() {
          var self = $(this);
          if (self.hasClass(levelClass) || typeof(levelClass) == "undefined") {
             self.show();
          } else {
             self.hide();
          }
       });
    });
 });
 