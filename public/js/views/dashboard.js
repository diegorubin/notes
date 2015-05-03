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

  addFolder: function(e) {
    e.preventDefault();

  },

  render: function() {
    this.collection.each(function(item) {
      this.renderDirectory(item);
    }, this);
    return this;
  },

  renderDirectoryfunction(item) {
  }
});
