package Notes::Model::Document;

# class methods
sub new {
  my $this = shift;
  my $class = ref($this) || $this;

  my $self = {
      title => shift,
      path => shift,
      version => 0
  };

  return bless $self, $class;
}

sub from_path {
  my $this = shift;
  my $class = ref($this) || $this;

  my $action = shift;
  my $path = shift;

  return $action->model('notes.documents')->find({ path => $path });
}

# instance methods
sub title {
  my $self = shift;
  my $v = shift;
  $self->{title} = $v if ($v);
  return $self->{title};
}

sub path {
  my $self = shift;
  my $v = shift;
  $self->{path} = $v if ($v);
  return $self->{path};
}

sub version {
  my $self = shift;
  return $self->{version};
}

sub save {
  my $self = shift;
  my $action = shift;

  return $action->model('notes.documents')->insert(
    {title => $self.title(), path => $self.path()}
  );
}

1;
