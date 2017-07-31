{
  'targets': [
    {
      'target_name': 'kytea',
      'sources': ['src/node_kytea.cc', 'src/node_kytea_async.cc'],
      'include_dirs': ["<!(node -e \"require('nan')\")", "<!(pkg-config --cflags-only-I kytea | sed s/-I//g)"],
      'cflags': ['-fexceptions'],
      'cflags_cc': ['-fexceptions'],
      'cflags!': ['-fno-exceptions', '-fno-rtti'],
      'cflags_cc!': ['-fno-exception', '-fno-rtti'],
      'libraries': ["<!(pkg-config --libs kytea)", "<!(pkg-config --libs-only-L kytea | sed s/^-L/-Wl,-rpath,/)"],
      'conditions': [
        ['OS=="mac"', {
            'xcode_settings': {
              'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
              'GCC_ENABLE_CPP_RTTI': 'YES'
            }
          }
        ]
      ]
    }
  ]
}
