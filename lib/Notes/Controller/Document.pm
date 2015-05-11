package Notes::Controller::Document;
use Mojo::Base 'Mojolicious::Controller';
use Notes::Model::Document;

sub index {
  my $self = shift;
  $self->render(status => 200, json => {});
}

sub create {
  my $self = shift;
  my $document = new Notes::Model::Document(
    $self->params('title'), $self->params('path'));

  if($document.save($self)) {
    $self->render(status => 200);
  } else {
    $self->render(status => 422);
  }
}

1;
