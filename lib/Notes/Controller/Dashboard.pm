package Notes::Controller::Dashboard;
use Mojo::Base 'Mojolicious::Controller';
use Notes::Model::Document;

sub index {
  my $self = shift;
  $self->render(path => '/');
}

1;
