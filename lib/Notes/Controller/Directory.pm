package Notes::Controller::Directory;
user Mojo::Base 'Mojolicious::Controller';

sub directories {
  my $self = shift;
  $self->render(json => {path => $self->param('path')}, status => 200);
}

1;
