from game.App import App


if __name__ == "__main__":
    app = App(800, 600, max_fps=60)
    app.run()