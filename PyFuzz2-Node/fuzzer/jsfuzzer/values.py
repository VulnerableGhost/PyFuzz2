# coding=utf8
__author__ = 'susperius'


class FuzzValues:
    INTERESTING_VALUES = ['0', '1', '5e6', '-7e6', '8e-6', '2e100', 'null', 'pink', 'false',
                          'true', '7500000000', '4400000000', '-4400000000', '-7500000000']

    CSS_STYLES = [['background-attachment', 'fixed', 'scroll'],
                  ['background-color', '#b0c4de', 'none'],
                  ['background-image', 'file:///c:/grinder/node/data/grind.jpg'],
                  ['background-position', 'size', '50% 50%', '10 10', 'left top', 'center top', 'inherit'],
                  ['background-repeat', 'repeat', 'repeat-x', 'repeat-y', 'no-repeat'],
                  ['border', 'solid', 'double', 'groove', 'dotted', 'dashed', 'inset', 'outset', 'ridge', 'hidden',
                   'four-sides', '5px'],
                  ['border-bottom', '5px', '#b0c4de', 'thick'],
                  ['border-bottom-color', '#b0c4de'],
                  ['border-bottom-style', 'solid', 'double', 'groove', 'dotted', 'dashed', 'inset', 'outset', 'ridge',
                   'hidden'],
                  ['border-bottom-width', '5px', 'thick'],
                  ['border-color', '#b0c4de'],
                  ['border-left', '10px', '#ff0000', 'thin'],
                  ['border-left-color', '#ff0000'],
                  ['border-left-style', 'solid', 'double', 'groove', 'dotted', 'dashed', 'inset', 'outset', 'ridge',
                   'hidden'],
                  ['border-left-width', '10px', 'thin'],
                  ['border-right', '5px', '#b0c4de', 'thin'],
                  ['border-right-color', '#b0c4de'],
                  ['border-right-style', 'solid', 'double', 'groove', 'dotted', 'dashed', 'inset', 'outset', 'ridge',
                   'hidden'],
                  ['border-right-width', '5px', 'thin'],
                  ['border-style', 'solid', 'double', 'groove', 'dotted', 'dashed', 'inset', 'outset', 'ridge',
                   'hidden', 'four-sides', 'thick'],
                  ['border-top', '5px', '#b0c4de', 'thick'],
                  ['border-top-color', '#b0c4de'],
                  ['border-top-style', 'solid', 'double', 'groove', 'dotted', 'dashed', 'inset', 'outset', 'ridge',
                   'hidden'],
                  ['border-top-width', '5px', 'thick'],
                  ['border-width', '5px', 'thick'],
                  ['clear', 'left', 'right', 'both'],
                  ['color', '#b0c4de'],
                  ['display', 'block', 'inline'],
                  ['float', 'left', 'right'],
                  ['font-family', 'Georgia'],
                  ['font-size', '100%', '10px', 'small', 'inherit'],
                  ['font-style', 'italic', 'oblique', 'normal'],
                  ['font-variant', 'small-caps'],
                  ['font-weight', 'bold', '900'],
                  ['height', '100px', 'auto'],
                  ['letter-spacing', '2px'],
                  ['line-height', '2', '90%'],
                  ['list-style', 'circle', 'square', 'disc', 'upper-alpha', 'lower-alpha', 'upper-roman', 'lower-roman',
                   'decimal', 'inside', 'outside', 'none'],
                  ['list-style-image', 'file:///c:/pyfuzz/fuzzer/background.jpg'],
                  ['list-style-position', 'inside', 'outside'],
                  ['list-style-type', 'circle', 'square', 'disc', 'upper-alpha', 'lower-alpha', 'upper-roman',
                   'lower-roman', 'decimal'],
                  ['margin', '5px', '10%', 'auto'],
                  ['margin-bottom', '2px', '30%', 'auto'],
                  ['margin-left', '5px', '50%', 'auto'],
                  ['margin-right', '5px', '50%', 'auto'],
                  ['margin-top', '10px', '60%', 'auto'],
                  ['padding', '5px', '100%', 'four-sides'],
                  ['padding-bottom', '10px', '100%'],
                  ['padding-left', '5px', '40%'],
                  ['padding-right', '6px', '100%'],
                  ['padding-top', '10px', '40%'],
                  ['position', 'absolute', 'relative', '100%', '100px'],
                  ['text-align', 'right', 'center', 'left', 'justify'],
                  ['text-decoration', 'line-through', 'overline', 'underline', 'none'],
                  ['text-indent', '5px', '5%'],
                  ['text-transform', 'capitalize', 'lowercase', 'uppercase'],
                  ['vertical-align', 'vertical-values'],
                  ['white-space', 'nowrap'],
                  ['width', '100pz', '100%', 'auto'],
                  ['word-spacing', '2px'],
                  ['z-index', '1']]
