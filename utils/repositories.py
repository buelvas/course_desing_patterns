import json

class BaseRepository:
    def __init__(self, db_file):
        self.db_file = db_file
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.db_file, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(f"ERROR: Failed to load data from {self.db_file}: {str(e)}")
            return {}

    def save_data(self):
        with open(self.db_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def get_all(self, entity_name):
        return self.data.get(entity_name, [])

    def get_by_id(self, entity_name, id):
        return next((item for item in self.data.get(entity_name, []) if item['id'] == id), None)

    def add(self, entity_name, item):
        self.data.setdefault(entity_name, []).append(item)
        self.save_data()

    def delete(self, entity_name, id):
        self.data[entity_name] = [item for item in self.data.get(entity_name, []) if item['id'] != id]
        self.save_data()


class ProductRepository(BaseRepository):
    def __init__(self, db_file='db.json'):
        super().__init__(db_file)
        self.entity_name = 'products'

    def get_all(self):
        return super().get_all(self.entity_name)

    def get_by_id(self, id):
        return super().get_by_id(self.entity_name, id)

    def get_products_by_category(self, category):
        return [item for item in self.get_all() if item.get('category') == category]

    def add(self, item):
        super().add(self.entity_name, item)

    def delete(self, id):
        super().delete(self.entity_name, id)


class CategoryRepository(BaseRepository):
    def __init__(self, db_file='db.json'):
        super().__init__(db_file)
        self.entity_name = 'categories'

    def get_all(self):
        return super().get_all(self.entity_name)

    def get_by_id(self, id):
        return super().get_by_id(self.entity_name, id)

    def add(self, item):
        super().add(self.entity_name, item)

    def delete(self, id):
        super().delete(self.entity_name, id)


class FavoriteRepository(BaseRepository):
    def __init__(self, db_file='db.json'):
        super().__init__(db_file)
        self.entity_name = 'favorites'

    def get_all(self):
        return super().get_all(self.entity_name)

    def get_by_id(self, id):
        return super().get_by_id(self.entity_name, id)

    def add(self, item):
        super().add(self.entity_name, item)

    def delete(self, id):
        super().delete(self.entity_name, id)
