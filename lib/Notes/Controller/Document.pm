package Notes::Controller::Document;
use Mojo::Base 'Mojolicious::Controller';
use Notes::Model::Document;

sub index {
  my $self = shift;
  my $path = $self->param('path');

  my $cursor = all Notes::Model::Document($self, $path);
  my $result = [];

  while(my $document = $cursor->next) {
    push $result, $document;
  }

  $self->render(status => 200, json => $result);
}

sub create {
  my $self = shift;
  my $document = new Notes::Model::Document(
    $self->params('title') || "Without Title", 
    $self->params('path') || "/");

  if($document.save($self)) {
    $self->render(status => 200, document => $document->to_hash());
  } else {
    $self->render(status => 422);
  }
}

1;
