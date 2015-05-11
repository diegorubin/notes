package Notes::Controller::Directory;
use Mojo::Base 'Mojolicious::Controller';

sub index {
  my $self = shift;
  $self->render(json => {path => $self->param('path')}, status => 200);
}

1;
