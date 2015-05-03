package Notes::Controller::Dashboard;
use Mojo::Base 'Mojolicious::Controller';
use Notes::Model::Document;

# This action will render a template
sub index {
  my $self = shift;

  my $document = new Notes::Model::Document();
  $document->title('teste');
  $document->save($self);

  # Render template "example/welcome.html.ep" with message
  $self->render(msg => 'Welcome to the Mojolicious real-time web framework!');
}

1;
