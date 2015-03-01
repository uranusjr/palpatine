========
Usage
========

To use Palpatine in a project::

    import palpatine
    palpatine.init()


Clear the screen::

    palpatine.screen.clear()


Move the cursor around and do things::

    palpatine.cursor.move(5, 3)
    print('Hello world!')
    print('A second line.')


Move the cursor relatively::

    palpatine.cursor.up(bol=True)


Clear a line::

    palpatine.line.clear()
