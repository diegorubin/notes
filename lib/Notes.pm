package Notes;
use Mojo::Base 'Mojolicious';
use MongoDB::Connection;

# This method will run once at server start
sub startup {
  my $self = shift;

  # Documentation browser under "/perldoc"
  $self->plugin('PODRenderer');

  # MongoDB
  $self->plugin('mongodb', { 
    host => 'localhost',
    port => 27017,
    helper => 'db'
  });

  # Router
  my $r = $self->routes;

  # Normal route to controller
  $r->get('/')->to('dashboard#index');

  $r->get('/api/directories')->to('directory#index');

  $r->get('/api/documents')->to('document#index');
  $r->post('/api/documents')->to('document#create');

}

1;
