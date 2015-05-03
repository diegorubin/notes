package Notes::Controller::Dashboard;
use Mojo::Base 'Mojolicious::Controller';
use Notes::Model::Document;

# This action will render a template
sub index {
  my $self = shift;
  $self->render(path => '/');
}

sub directories {
  my $self = shift;
  $self->render(json => {path => $self->param('path')}, status => 200);
}

1;
