from app_tables import site_tables
# app.config['SECRET_KEY']

if __name__ == "__main__":
    site_tables.app.run(debug=True)  