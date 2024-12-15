from utils.repositories import ProductRepository, CategoryRepository, FavoriteRepository

_product_repo = ProductRepository()
_category_repo = CategoryRepository()
_favorite_repo = FavoriteRepository()

def get_repository(entity_type):
    repositories = {
        'products': _product_repo,
        'categories': _category_repo,
        'favorites': _favorite_repo
    }
    repo = repositories.get(entity_type)
    if not repo:
        raise ValueError(f"Repository for {entity_type} not found.")
    return repo
