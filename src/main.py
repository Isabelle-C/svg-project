from svg_project.util import Util

def main():
    Util.convert_svg_to_png('./figs/symbol/arrow.svg', './figs/symbol/arrow.png')

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()