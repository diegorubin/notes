'use strict';

var app = app || {};

app.Document = Backbone.Model.extend({
  validate: function(attrs, options) {
    this.errors = {};
    if (!attrs.path) {
      return this.errors['path'] = '';
    }
  }
});

