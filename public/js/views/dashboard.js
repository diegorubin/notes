var app = app || {};

app.DashboardView = Backbone.View.extend({
  el: $('body'),

  initialize: function() {
    this.collection = new app.DocumentCollection();
    this.collection.fetch();
    this.render();

    this.listenTo(this.collection, 'add', this.render);
  },

  events: {
    'click #add-directory': 'addDirectory',
    'click #add-document': 'addDocument'
  },

  addDocument: function(e) {
    e.preventDefault();
    this.documentView();
  },

  addDirectory: function(e) {
    e.preventDefault();
  },

  render: function() {
    this.collection.each(function(item) {
      this.renderDirectory(item);
    }, this);
    return this;
  },

  renderDirectory: function(item) {
  },

  documentView: function() {
    $('.sidebar').hide();
    $('#directory-content').hide();
    $('#document-content').show();

    var remove = [
      'col-sm-9', 'col-sm-offset-3', 'col-md-10', 'col-md-offset-2'
    ];

    var add = ['col-sm-12', 'col-md-12'];

    $.each(remove, function(index,klass) { $('.main').removeClass(klass); });
    $.each(add, function(index,klass) { $('.main').addClass(klass); });
  },

  directoryView: function() {
  }
});
