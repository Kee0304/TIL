- annotate: 보통 aggregation과 함께 써서 어떠한 하나의 값을 가져올 때
  `articles = Article.objects.annotate(Count('comment')).order_by('-pk')`
- select_related: 나와 연관된 하나의 인스턴스에 대한 레코드를 가져올 때
  `articles = Article.objects.select_related('user').order_by('-pk')`
- prefetch_related: 나와 연관된 여러 개의 인스턴스에 대한 레코드들을 가져올 때
  `articles = Article.objects.prefetch_related('comment_set').order_by('-pk')`